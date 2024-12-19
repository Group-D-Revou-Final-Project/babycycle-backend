from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from

from src.services.transactions_service import (
    get_all_transactions,
    get_transaction_by_id,
    delete_transaction
)

transactions_bp = Blueprint('transactions', __name__)


@transactions_bp.route('/transactions', methods=['GET'])
@jwt_required()
def get_all_transactions_route():
    userID = get_jwt_identity()
    return get_all_transactions(user_id=userID)


@transactions_bp.route('/transactions/<string:checkout_id>', methods=['GET'])
@jwt_required()
def get_transaction_by_id_route(checkout_id):
    userID = get_jwt_identity()
    return get_transaction_by_id(user_id=userID, checkout_id=checkout_id)

@transactions_bp.route('/transactions/<string:checkout_id>', methods=['DELETE'])
@jwt_required()
def delete_transaction_route(checkout_id):
    userID = get_jwt_identity()
    return delete_transaction(user_id=userID, checkout_id=checkout_id)
   