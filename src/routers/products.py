from flask import Blueprint, request, jsonify
from flasgger import swag_from

from src.services.products_service import (
    get_all_products,
    get_product_by_id,
    create_product,
    update_product,
    delete_product,
    deactivate_product,
    get_all_products_limit_offset,
    user_has_product,
    get_products_by_sorting,
    get_products_by_category,
    get_product_by_warranty
)

from src.swagger.products_swagger import (
    GET_ALL_PRODUCTS,
    GET_PRODUCT_BY_ID,
    CREATE_PRODUCT,
    UPDATE_PRODUCT,
    DELETE_PRODUCT,
    DEACTIVATE_PRODUCT,
    GET_PRODUCTS_BY_SORTING,
    GET_PRODUCTS_BY_CATEGORY,
    GET_PRODUCTS_BY_WARRANTY
)

products_bp = Blueprint('products', __name__)

@products_bp.route('/products', methods=['GET'])
@swag_from(GET_ALL_PRODUCTS)
# @jwt_required()
def get_all_products_route():
    return get_all_products()

@products_bp.route('/products/pagination', methods=['GET'])
def get_all_products_limit_offset_route():
    limit = request.args.get('limit', default=10, type=int)
    offset = request.args.get('offset', default=0, type=int)

    return get_all_products_limit_offset(limit=limit, offset=offset)



@products_bp.route('/products/<int:product_id>', methods=['GET'])
@swag_from(GET_PRODUCT_BY_ID)
def get_product_by_id_route(product_id):
    return get_product_by_id(product_id)

@products_bp.route('/products', methods=['POST'])
@swag_from(CREATE_PRODUCT)
def create_product_route():    
    try:
        # Get data from the request
        data = request.get_json()

        # Extract fields
        name = data.get('name')
        price = data.get('price')
        descriptions = data.get('description', '')  # Optional field, defaults to an empty string
        category = data.get('category')
        stock = data.get('stock', 0)
        is_warranty = data.get('is_warranty', False)  # Optional field, defaults to False
        image_url = data.get('image_url', '')  # Optional field, defaults to an empty string
        # user_id = data.get('user_id')

        # Validate required fields
        if not name or not price or not category or not stock:
            return jsonify({"error": "Name, price, category and stock."}), 400

        # Pass the data to the service function
        return create_product(
            name=name,
            price=price,
            descriptions=descriptions,
            category=category,
            is_warranty=is_warranty, 
            image_url=image_url,
            stock=stock
            # user_id=user_id
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@products_bp.route('/products/<int:product_id>', methods=['PUT'])
@swag_from(UPDATE_PRODUCT)
def update_product_route(product_id):
    try:
        # Get data from the request
        data = request.get_json()

        # Extract fields
        name = data.get('name')
        price = data.get('price')
        descriptions = data.get('descriptions', '')  # Optional field, defaults to an empty string
        category = data.get('category')
        stock = data.get('stock', 0)
        is_warranty = data.get('is_warranty', False)  # Optional field, defaults to False
        image_url = data.get('image_url', '')  # Optional field, defaults to an empty string

        # Validate required fields
        if not name or not price or not category:
            return jsonify({"error": "Name, price, and category are required."}), 400

        # Pass the data to the service function
        return update_product(
            product_id=product_id,
            name=name,
            price=price,
            descriptions=descriptions,
            category=category,
            is_warranty=is_warranty, 
            image_url=image_url,
            stock=stock
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@products_bp.route('/products/<int:product_id>', methods=['DELETE'])
@swag_from(DELETE_PRODUCT)
def delete_product_route(product_id):
    return delete_product(product_id)

@products_bp.route('/products/<int:product_id>/deactivate', methods=['PUT'])
@swag_from(DEACTIVATE_PRODUCT)
def deactivate_product_route(product_id):
    return deactivate_product(product_id)

@products_bp.route('/products/users/has_products', methods=['POST'])
def user_has_products_route():
    data = request.get_json()
    email = data.get('email')
    return user_has_product(email=email)

@products_bp.route('/products/sorting', methods=['GET'])
@swag_from(GET_PRODUCTS_BY_SORTING)
def get_products_by_sorting_route():
    limit = request.args.get('limit', default=10, type=int)
    offset = request.args.get('offset', default=0, type=int)
    sort_by = request.args.get('sort_by', default="stock", type=str)

    return get_products_by_sorting(sort_by=sort_by, limit=limit, offset=offset)

@products_bp.route('/products/category', methods=['GET'])
@swag_from(GET_PRODUCTS_BY_CATEGORY)
def get_products_by_category_route():
    limit = request.args.get('limit', default=10, type=int)
    offset = request.args.get('offset', default=0, type=int)
    category = request.args.get('category', type=str)

    return get_products_by_category(category=category, limit=limit, offset=offset)
@products_bp.route('/products/warranty', methods=['GET'])
@swag_from(GET_PRODUCTS_BY_WARRANTY)
def get_products_by_warranty():
    limit = request.args.get('limit', default=10, type=int)
    offset = request.args.get('offset', default=0, type=int)
    # is_warranty = request.args.get('is_warranty', default=True, type=bool)
    is_warranty = request.args.get('is_warranty', default="true").lower() in ["true", "1", "yes"]

    return get_product_by_warranty(is_warranty=is_warranty, limit=limit, offset=offset)

