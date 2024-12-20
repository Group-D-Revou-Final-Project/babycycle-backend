from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from

from src.services.search_service import (
    search_products
)

from src.swagger.search_swagger import (
    SEARCH_PRODUCTS
)

search_bp = Blueprint('search', __name__)

@search_bp.route('/search/products', methods=['GET'])
@swag_from(SEARCH_PRODUCTS)
def search_route():
    query = request.args.get('query')
    limit = request.args.get('limit', default=10, type=int)
    offset = request.args.get('offset', default=0, type=int)
    
    return search_products(query=query, limit=limit, offset=offset)