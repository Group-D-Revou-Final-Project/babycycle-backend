from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from

from src.services.transactions_service import (
    get_all_transactions,
    get_transaction_by_id,
    delete_transaction,
    get_all_transactions_by_seller
)

from src.swagger.transactions_swagger import (
    GET_ALL_TRANSACTIONS,
    GET_TRANSACTION_BY_ID,
    DELETE_TRANSACTION,
    GET_ALL_TRANSACTIONS_BY_SELLER
)

transactions_bp = Blueprint('transactions', __name__)


@transactions_bp.route('/transactions', methods=['GET'])
@jwt_required()
@swag_from(GET_ALL_TRANSACTIONS)
def get_all_transactions_route():
    userID = get_jwt_identity()
    return get_all_transactions(user_id=userID)


@transactions_bp.route('/transactions/<string:checkout_id>', methods=['GET'])
@swag_from(GET_TRANSACTION_BY_ID)
@jwt_required()
def get_transaction_by_id_route(checkout_id):
    userID = get_jwt_identity()
    return get_transaction_by_id(user_id=userID, checkout_id=checkout_id)

@transactions_bp.route('/transactions/<string:checkout_id>', methods=['DELETE'])
@swag_from(DELETE_TRANSACTION)
@jwt_required()
def delete_transaction_route(checkout_id):
    userID = get_jwt_identity()
    return delete_transaction(user_id=userID, checkout_id=checkout_id)

@transactions_bp.route('/transactions/seller', methods=['GET'])
@swag_from(GET_ALL_TRANSACTIONS_BY_SELLER)
@jwt_required()  
def get_all_transactions_by_seller_route():
    userID = get_jwt_identity()
    return get_all_transactions_by_seller(user_id=userID)
   