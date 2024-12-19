from flask import Blueprint, request, jsonify
from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.services.seller_service import (
    get_sellers,
    get_seller_by_id,
    create_seller,
    update_seller,
    delete_seller,
    get_products_by_seller
)


sellers_bp = Blueprint('sellers', __name__)

@sellers_bp.route('/sellers', methods=['GET'])
@jwt_required()
def get_all_sellers_route():
    return get_sellers()


@sellers_bp.route('/sellers/<int:seller_id>', methods=['GET'])
@jwt_required()
def get_seller_by_id_route(seller_id):
    return get_seller_by_id(seller_id)


@sellers_bp.route('/sellers', methods=['POST'])
@jwt_required()
def create_seller_route():
    data = request.get_json()
    user_id = data.get('user_id')
    name = data.get('name')
    address = data.get('address')
    contact = data.get('contact')
    return create_seller(user_id=user_id, name=name, address=address, contact=contact)

@sellers_bp.route('/sellers/<int:seller_id>', methods=['PUT'])
@jwt_required()
def update_seller_route(seller_id):
    data = request.get_json()
    name = data.get('name')
    address = data.get('address')
    contact = data.get('contact')
    return update_seller(seller_id, name, address, contact)

@sellers_bp.route('/sellers/<int:seller_id>', methods=['DELETE'])
@jwt_required()
def delete_seller_route(seller_id):
    return delete_seller(seller_id)

@sellers_bp.route('/sellers/products', methods=['GET'])
@jwt_required()
def get_products_by_seller_route():
    user_id = get_jwt_identity()
    return get_products_by_seller(user_id)