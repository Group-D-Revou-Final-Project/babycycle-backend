from flask import jsonify
from src.models.orders_model import OrderModel
from src.models.order_items_model import OrderItemModel
from src.models.products_model import ProductModel
from src.models.sellers_model import SellerModel
from sqlalchemy import func
from src.config.settings import db

def get_all_transactions(user_id):
    # Perform the query using SQLAlchemy ORM
    results = db.session.query(
        OrderModel.user_id,
        OrderModel.seller_id,
        OrderModel.status,
        OrderModel.payment_method,
        OrderModel.checkout_id,
        OrderModel.created_at,
        OrderItemModel.product_id,
        OrderItemModel.total_price,
        OrderItemModel.user_address,
        OrderItemModel.quantity,
        ProductModel.name
    ).join(
        OrderItemModel, OrderModel.checkout_id == OrderItemModel.checkout_order_id
    ).join(
        ProductModel, OrderItemModel.product_id == ProductModel.id
    ).filter(
        OrderModel.user_id == user_id
    ).all()

    if not results:
        return jsonify({"error": "No transactions found for the specified user"}), 404

    # Format the results as a list of dictionaries
    formatted_results = [
        {
            "user_id": result[0],
            "seller_id": result[1],
            "status": result[2],
            "payment_method": result[3],
            "checkout_id": result[4],
            "created_at": result[5].isoformat(),  # Format created_at as ISO 8601 string
            "product_id": result[6],
            "total_price": result[7],
            "user_address": result[8],
            "quantity": result[9],
            "name": result[10]
        }
        for result in results
    ]

    return jsonify(formatted_results), 200



def get_transaction_by_id(user_id, checkout_id):
    results = db.session.query(
        OrderModel.user_id,
        OrderModel.seller_id,
        OrderModel.status,
        OrderModel.payment_method,
        OrderModel.checkout_id,
        OrderModel.created_at,
        OrderItemModel.product_id,
        OrderItemModel.total_price,
        OrderItemModel.user_address,
        OrderItemModel.quantity,
        ProductModel.name
    ).join(
        OrderItemModel, OrderModel.checkout_id == OrderItemModel.checkout_order_id
    ).join(
        ProductModel, OrderItemModel.product_id == ProductModel.id
    ).filter(
        OrderModel.checkout_id == checkout_id,
        OrderModel.user_id == user_id
    ).all()

    if not results:
        return jsonify({"error": "Transaction not found"}), 404

   # Format the results as a list of dictionaries
    formatted_results = [
        {
            "user_id": result[0],
            "seller_id": result[1],
            "status": result[2],
            "payment_method": result[3],
            "checkout_id": result[4],
            "created_at": result[5].isoformat(),  # Format created_at as ISO 8601 string
            "product_id": result[6],
            "total_price": result[7],
            "user_address": result[8],
            "quantity": result[9],
            "name": result[10]
        }
        for result in results
    ]

    return jsonify(formatted_results), 200

def delete_transaction(user_id, checkout_id):
    transaction = OrderModel.query.filter_by(checkout_id=checkout_id, user_id=user_id).first()
    if not transaction:
        return jsonify({"error": "Transaction not found"}), 404
    db.session.delete(transaction)
    db.session.commit()
    return jsonify({"message": "Transaction deleted successfully"})


def get_all_transactions_by_seller(user_id):
    seller = SellerModel.query.filter_by(user_id=user_id).first()

    if not seller:
        return jsonify({"error": "Seller not found"}), 404
    
        # Perform the query using SQLAlchemy ORM
    total_transactions = OrderModel.query.filter_by(seller_id=seller.id).count()

    product_listed = ProductModel.query.filter_by(seller_id=seller.id).count()

    products_sold = db.session.query(
        func.sum(OrderItemModel.quantity).label("total_product_sold")
    ).join(
        OrderModel, OrderItemModel.checkout_order_id == OrderModel.checkout_id
    ).filter(
        OrderModel.seller_id == seller.id
    ).scalar()

    return jsonify({"total_transactions": total_transactions, "product_listed": product_listed, "products_sold": products_sold}), 200




#     if not transaction_count:
#         return jsonify({"error": "No transactions found for the specified seller"}), 404

#     # Format the results as a list of dictionaries
#     formatted_results = [
#         {
#             "user_id": result[0],
#             "seller_id": result[1],
#             "status": result[2],
#             "payment_method": result[3],
#             "checkout_id": result[4],
#             "created_at": result[5].isoformat(),  # Format created_at as ISO 8601 string
#             "product_id": result[6],
#             "total_price": result[7],
#             "user_address": result[8],
#             "quantity": result[9],
#             "name": result[10]
#         }
#         for result in results
#     ]

#     return jsonify(formatted_results), 200
    
