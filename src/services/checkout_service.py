from flask_jwt_extended import create_access_token, get_jwt_identity
from flask import jsonify
from src.config.settings import db
from src.models.orders_model import OrderModel
from src.models.order_items_model import OrderItemModel
from src.models.products_model import ProductModel

def checkout_now(cart_items, payment_method):
    
    seller_groups = {}
    for item in cart_items:
        product = Product.query.get(item['product_id'])
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
