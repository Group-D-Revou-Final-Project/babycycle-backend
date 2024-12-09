from flask import Blueprint, request, jsonify
from flasgger import swag_from

from src.services.products_service import (
    deactivate_product,
    delete_product,
    get_all_products,
    get_product_by_id,
    create_product,
    update_product
)

from src.swagger.products_swagger import (
    GET_ALL_PRODUCTS,
    GET_PRODUCT_BY_ID,
    CREATE_PRODUCT,
    UPDATE_PRODUCT,
    DELETE_PRODUCT,
    DEACTIVATE_PRODUCT
)

products_bp = Blueprint('products', __name__)

@products_bp.route('/products', methods=['GET'])
@swag_from(GET_ALL_PRODUCTS)
def get_all_products_route():
    return get_all_products()

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
        description = data.get('description', '')  # Optional field, defaults to an empty string
        category = data.get('category')
        stock = data.get('stock', 0)
        is_warranty = data.get('is_warranty', False)  # Optional field, defaults to False
        image_url = data.get('image_url', '')  # Optional field, defaults to an empty string

        # Validate required fields
        if not name or not price or not category or not stock:
            return jsonify({"error": "Name, price, category and stock."}), 400

        # Pass the data to the service function
        return create_product(
            name=name,
            price=price,
            description=description,
            category=category,
            is_warranty=is_warranty, 
            image_url=image_url,
            stock=stock
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
        description = data.get('description', '')  # Optional field, defaults to an empty string
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
            description=description,
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