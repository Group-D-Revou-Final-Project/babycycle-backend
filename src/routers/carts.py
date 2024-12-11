from flask import Blueprint, request, jsonify
from flasgger import swag_from

from src.services.carts_service import (
    get_all_carts,
    get_cart_by_id,
    create_cart,
    update_cart,
    delete_cart
)
from src.swagger.carts_swagger import (
    DELETE_CARTS,
    GET_CARTS,
    GET_CARTS_BY_ID,
    UPDATE_CARTS,
    CREATE_CARTS
)

carts_bp = Blueprint('carts', __name__)

@carts_bp.route('/carts', methods=['GET'])
@swag_from(GET_CARTS)
def cart_route_get_all():
    return get_all_carts()

   
@carts_bp.route('/carts', methods=['POST'])
@swag_from(CREATE_CARTS)
def cart_route_post():
    data = request.get_json()
    product_id = data.get('product_id')
    user_id = data.get('user_id')
    quantity = data.get('quantity')
    user_address = data.get('user_address')
    total_price = data.get('total_price')

    return create_cart(product_id=product_id, user_id=user_id, quantity=quantity, user_address=user_address, total_price=total_price)

@carts_bp.route('/carts/<int:cart_id>', methods=['GET'])
@swag_from(GET_CARTS_BY_ID)
def cart_route_get_cart_by_id(cart_id):
    return get_cart_by_id(cart_id=cart_id)

@carts_bp.route('/carts/<int:cart_id>', methods=['PUT'])
@swag_from(UPDATE_CARTS)
def cart_route_update(cart_id):
    data = request.get_json()
    quantity = data.get('quantity')
    total_price = data.get('total_price')

    return update_cart(cart_id=cart_id, quantity=quantity, total_price=total_price)
@carts_bp.route('/carts/<int:cart_id>', methods=['DELETE'])
@swag_from(DELETE_CARTS)
def cart_route_delete(cart_id):
    return delete_cart(cart_id=cart_id)