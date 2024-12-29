from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from


from src.services.address_service import (
    get_address_by_user,
    create_address,
    get_address_by_id,
    update_address_by_id,
    delete_address_by_id,
    set_main_address

)
address_bp = Blueprint('address', __name__)

@address_bp.route('/addresses', methods=['GET'])
# @swag_from(GET_ALL_ADDRESSES)
@jwt_required()
def get_address_by_user_route():
    userID = get_jwt_identity()
    return get_address_by_user(user_id=userID)


@address_bp.route('/addresses', methods=['POST'])
# @swag_from(CREATE_ADDRESS)
@jwt_required()
def create_address_route():
    userID = get_jwt_identity()
    data = request.get_json()

    # Ensure data is a list
    if not isinstance(data, list):
        return jsonify({"error": "Expected a list of addresses"}), 400

    # Pass the entire data list to the create_address function
    return create_address(user_id=userID, addresses=data)


@address_bp.route('/addresses/<int:address_id>', methods=['PUT'])
# @swag_from(UPDATE_ADDRESS_BY_ID)
@jwt_required()
def update_address_by_id_route(address_id):
    userID = get_jwt_identity()
    data = request.get_json()
    if not isinstance(data, list):
        return jsonify({"error": "Expected a list of addresses"}), 400
    
    return update_address_by_id(id=address_id, user_id=userID, addresses=data)


@address_bp.route('/addresses/<int:address_id>', methods=['GET'])
# @swag_from(GET_ADDRESS_BY_ID)
@jwt_required()
def get_address_by_id_route(address_id):
    userID = get_jwt_identity()
    return get_address_by_id(id=address_id, user_id=userID)

@address_bp.route('/addresses/<int:address_id>', methods=['DELETE'])
# @swag_from(DELETE_ADDRESS_BY_ID)
@jwt_required()
def delete_address_by_id_route(address_id):
    userID = get_jwt_identity()
    return delete_address_by_id(id=address_id, user_id=userID)

@address_bp.route('/addresses/set-as-main/<int:address_id>', methods=['PUT'])
# @swag_from(DELETE_ADDRESS_BY_ID)
@jwt_required()
def set_main_address_by_id_route(address_id):
    userID = get_jwt_identity()
    return set_main_address(id=address_id, user_id=userID)
