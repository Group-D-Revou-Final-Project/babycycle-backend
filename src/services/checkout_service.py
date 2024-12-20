from flask_jwt_extended import create_access_token, get_jwt_identity
from flask import jsonify
from src.models.users_model import UserModel
from src.config.settings import db
from src.models.orders_model import OrderModel
from src.models.order_items_model import OrderItemModel
from src.models.products_model import ProductModel
# from src.models.sellers_model import SellerModel
from src.models.carts_model import CartModel


def checkout_now(cart_items, payment_method, current_user_id):
    
    seller_groups = {}
    for item in cart_items:
        product = ProductModel.query.get(item['product_id'])
        if product:
            seller_id = product.seller_id
            if seller_id not in seller_groups:
                seller_groups[seller_id] = []
            seller_groups[seller_id].append({
                'product': product,
                'quantity': item['quantity'],
                'total_price': product.price * item['quantity']
            })

    # Menyimpan pesanan dan mengurangi stok produk
    orders = []
    for seller_id, items in seller_groups.items():
        total_price = sum(item['total_price'] for item in items)

        # Buat order untuk seller ini
        order = OrderModel(user_id=current_user_id, seller_id=seller_id, total_price=total_price, payment_method=payment_method, status='paid')
        db.session.add(order)
        db.session.commit()

        # Bikin order items untuk setiap produk yang dibeli
        for item in items:
            order_item = OrderItemModel(
                order_id=order.id,
                product_id=item['product'].id,
                quantity=item['quantity'],
                price=item['product'].price
            )
            db.session.add(order_item)

            # Cek apakah stok cukup
            if item['product'].stock < item['quantity']:
                db.session.rollback()  # Batalkan transaksi jika stok tidak cukup
                return jsonify({"error": f"Not enough stock for {item['product'].name}"}), 400

            # Kurangi stok produk
            item['product'].stock -= item['quantity']
            db.session.commit()  # Simpan perubahan stok

        db.session.commit()  # Commit transaksi untuk seller ini
        orders.append(order)

   
    return jsonify({
        "message": "Checkout successful",
        "orders": [{"order_id": order.id, "total_price": order.total_price, "status": order.status} for order in orders]
    })

def checkout_item_now(checkout_id, payment_method, current_user_id):
    order = OrderModel.query.filter_by(checkout_id=checkout_id).first()
    if order:
        return jsonify({"error": "Transaction already exists"}), 400

    # Buat order
    order = OrderModel(user_id=current_user_id, payment_method=payment_method, status='paid', checkout_id=checkout_id)
    db.session.add(order)
    db.session.commit()


    return jsonify({
        "message": "Checkout successful",
        "order": {"order_id": order.id, "payment_method": order.payment_method,"status": order.status}
    })

def create_order_items(user_id, product_id, quantity, total_price, user_address, checkout_order_id):
    try:
        # Check if the user is verified
        user = UserModel.query.filter_by(id=user_id, is_verified=True).first()
        if not user:
            return {"error": "User not found or not verified"}, 404

        # Check if the product exists and is available
        product = ProductModel.query.filter_by(id=product_id, is_deleted=False, is_deactivated=False).first()
        if not product:
            return {"error": "Product not found or not available"}, 404

        # Check if there is enough stock
        if product.stock < quantity:
            return {"error": f"Not enough stock available for product {product_id}"}, 400

        # Check if the product is already in the user's order
        # current_order_item = OrderItemModel.query.filter_by(product_id=product_id, user_address=user_address).first()

        # if current_order_item:
        #     # Update the existing order item
        #     current_order_item.quantity = quantity
        #     current_order_item.total_price = total_price
        #     current_order_item.user_address = user_address
        #     current_order_item.checkout_order_id = checkout_order_id
        #     db.session.commit()

        #     return {
        #         "message": "Order item updated successfully",
        #         "data": current_order_item.to_dict()
        #     }, 200

        # Create a new order item
        new_order_item = OrderItemModel(
            product_id=product_id,
            quantity=quantity,
            total_price=total_price,
            user_address=user_address,
            checkout_order_id=checkout_order_id,
        )

        # Update the product's stock
        product.stock -= quantity

        # Add the new order item to the database
        db.session.add(new_order_item)
        db.session.commit()

        return {
            "message": "Order item created successfully",
            "data": new_order_item.to_dict()
        }, 201
    except Exception as e:
        db.session.rollback()
        return {"error": f"An error occurred function: {str(e)}"}, 500
    
def checkout_validate(user_id):
    # Retrieve all carts for the given user
    carts = CartModel.query.filter_by(user_id=user_id).all()

    if not carts:
        return jsonify({"error": "No items in the cart"}), 404

    # Retrieve all products related to the cart
    product_ids = [cart.product_id for cart in carts]
    products = ProductModel.query.filter(ProductModel.id.in_(product_ids)).all()

    # Create a mapping of product_id to stock for quick lookup
    product_stock_map = {product.id: product.stock for product in products}

    # Validate the cart quantities against product stocks
    for cart in carts:
        product_stock = product_stock_map.get(cart.product_id, 0)
        if cart.quantity > product_stock:
            return jsonify({
                "error": "Insufficient stock",
                "product_id": cart.product_id,
                "requested_quantity": cart.quantity,
                "available_stock": product_stock,
                "product_name": cart.product.name
            }), 400

    return jsonify({"message": "Validation successful"}), 200
   
