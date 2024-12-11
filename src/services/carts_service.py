from flask import jsonify
from src.models.products_model import ProductModel
from src.models.users_model import UserModel
from src.models.carts_model import CartModel
from src.config.settings import db


def get_all_carts():
    try:
        carts = CartModel.query.all()
        return jsonify([cart.to_dict() for cart in carts]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def get_cart_by_id(cart_id):
    try:
        cart = CartModel.query.filter_by(id=cart_id).first()
        if cart:
            return jsonify(cart.to_dict()), 200
        else:
            return jsonify({"error": "Cart not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def create_cart(user_id, product_id, quantity, total_price, user_address):
    try:
        # Create a new CartModel instance
        user = UserModel.query.filter_by(id=user_id, is_verified=True).first()
        product = ProductModel.query.filter_by(id=product_id, is_deleted=False, is_deactivated=False).first()

        if not user and not product:
            return jsonify({"error": "User or product not found"}), 404
        
        if product.stock < quantity:
            return jsonify({"error": "Not enough stock available"}), 400
        
        current_cart = CartModel.query.filter_by(user_id=user_id, product_id=product_id).first()
        if current_cart:
            return jsonify({"error": "Product already in cart"}), 400

        new_cart = CartModel(user_id=user_id, product_id=product_id, quantity=quantity, total_price=total_price, user_address=user_address)
        
        # Add to database
        db.session.add(new_cart)
        db.session.commit()
        
        # Return the created cart
        return jsonify(new_cart.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def update_cart(cart_id, quantity, total_price):
    try:
        cart = CartModel.query.filter_by(id=cart_id).first()
        if cart:
            cart.quantity = quantity
            cart.total_price = total_price
            db.session.commit()
            return jsonify(cart.to_dict()), 200
        else:
            return jsonify({"error": "Cart not found"}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
def delete_cart(cart_id):
    try:
        cart = CartModel.query.filter_by(id=cart_id).first()
        if cart:
            db.session.delete(cart)
            db.session.commit()
            return jsonify({"message": "Cart deleted successfully"}), 200
        else:
            return jsonify({"error": "Cart not found"}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500