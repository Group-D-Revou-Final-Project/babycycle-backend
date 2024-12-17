from flask import Blueprint, request, jsonify
from src.services.checkout_service import checkout_now
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.models.users_model import UserModel

@register_blueprint.route('/checkout', methods=['POST'])
@jwt_required()
def checkout():
    current_user_id = get_jwt_identity()  
    data = request.json
    cart_items = data.get('cart_items')
    payment_method = data.get('payment_method')

    user = User.query.get(current_user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return checkout_now(cart_items=cart_items, payment_method=payment_method)