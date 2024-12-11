from flask import Blueprint, request, jsonify
from flasgger import swag_from

from src.services.carts_service import (
    create_cart
)

carts_bp = Blueprint('carts', __name__)

@carts_bp.route('/carts', methods=['POST'])
def create_cart_route():
    data = request.get_json()
    product_id = data.get('product_id')
    user_id = data.get('user_id')
    quantity = data.get('quantity')
    user_address = data.get('user_address')
    total_price = data.get('total_price')

    return create_cart(product_id=product_id, user_id=user_id, quantity=quantity, user_address=user_address, total_price=total_price)