from flask import Blueprint
from flasgger import swag_from

from src.services.discount_service import (
    get_discount_by_id
)

from src.swagger.discounts_swagger import (
   GET_DISCOUNT_BY_ID
)

discount_bp = Blueprint('discount', __name__)

@discount_bp.route('/<int:product_id>', methods=['GET'])
@swag_from(GET_DISCOUNT_BY_ID)
def discount_route_get_by_id(product_id):
    return get_discount_by_id(product_id)

# @discount_bp.route('/calculated-price/<int:product_id>', methods=['GET'])
# @swag_from(GET_CALCULATED_DISCOUNT)
# def discount_route_calculate_discount(product_id):
#     return get_calculated_discount(product_id)