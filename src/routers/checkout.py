from flask import Blueprint, request, jsonify
from src.services.checkout_service import checkout_now
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.models.users_model import UserModel
from flasgger import swag_from

from src.swagger.checkout_swagger import (
    CHECKOUT
)


checkout_bp=Blueprint('checkout', __name__)
@checkout_bp.route('/checkout', methods=['POST'])
@jwt_required()
@swag_from(CHECKOUT)
def checkout():
    current_user_id = get_jwt_identity()  
    data = request.json
    cart_items = data.get('cart_items')
    payment_method = data.get('payment_method')

    user = UserModel.query.get(current_user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return checkout_now(cart_items=cart_items, payment_method=payment_method, current_user_id=current_user_id)