from flask import Blueprint, request
from flasgger import swag_from
from flask_jwt_extended import jwt_required

from src.services.discount_service import (
    get_discount_by_id,
    create_discount

)

from src.swagger.discounts_swagger import (
   GET_DISCOUNT_BY_ID,
   CREATE_DISCOUNT
)

discount_bp = Blueprint('discount', __name__)

@discount_bp.route('/<int:product_id>', methods=['GET'])
@swag_from(GET_DISCOUNT_BY_ID)
def discount_route_get_by_id(product_id):
    return get_discount_by_id(product_id)

@discount_bp.route('/', methods=['POST'])
@swag_from(CREATE_DISCOUNT)
@jwt_required()
def create_discount_route():
    data = request.get_json()
    product_id = data.get('product_id')
    discount_percentage = data.get('discount_percentage')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    is_active = data.get('is_active')

    return create_discount(product_id, discount_percentage, start_date, end_date, is_active)

# @discount_bp.route('/calculated-price/<int:product_id>', methods=['GET'])
# @swag_from(GET_CALCULATED_DISCOUNT)
# def discount_route_calculate_discount(product_id):
#     return get_calculated_discount(product_id)