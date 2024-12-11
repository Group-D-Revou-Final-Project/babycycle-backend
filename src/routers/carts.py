from flask import Blueprint, request, jsonify
from flasgger import swag_from

from src.services.carts_service import (
    get_all_carts,
    get_cart_by_id,
    create_cart,
    update_cart,
    delete_cart
)

carts_bp = Blueprint('carts', __name__)

@carts_bp.route('/carts', methods=['POST', 'GET'])
def cart_route_post_get():
    if request.method == 'GET':
        return get_all_carts()
    elif request.method == 'POST':
        data = request.get_json()
        product_id = data.get('product_id')
        user_id = data.get('user_id')
        quantity = data.get('quantity')
        user_address = data.get('user_address')
        total_price = data.get('total_price')

        return create_cart(product_id=product_id, user_id=user_id, quantity=quantity, user_address=user_address, total_price=total_price)

@carts_bp.route('/carts/<int:cart_id>', methods=['PUT', 'GET', 'DELETE'])
def cart_route_put_get_delete(cart_id):
    if request.method == 'PUT':
        data = request.get_json()
        quantity = data.get('quantity')
        total_price = data.get('total_price')

        return update_cart(cart_id=cart_id, quantity=quantity, total_price=total_price)
    elif request.method == 'GET':
        return get_cart_by_id(cart_id=cart_id)
    elif request.method == 'DELETE':
        return delete_cart(cart_id=cart_id)