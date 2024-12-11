from flask import jsonify
from src.models.products_model import ProductModel
from src.models.users_model import UserModel
from src.models.carts_model import CartModel
from src.config.settings import db

def create_cart(user_id, product_id, quantity, total_price, user_address):
    try:
        # Create a new CartModel instance
        user = UserModel.query.get(user_id)
        product = ProductModel.query.get(product_id)

        if not user and not product:
            return jsonify({"error": "User or product not found"}), 404

        new_cart = CartModel(user_id=user_id, product_id=product_id, quantity=quantity, total_price=total_price, user_address=user_address)
        
        # Add to database
        db.session.add(new_cart)
        db.session.commit()
        
        # Return the created cart
        return jsonify(new_cart.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500