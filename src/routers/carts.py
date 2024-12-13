from flask import Blueprint, request, jsonify
from flasgger import swag_from

from src.services.carts_service import (
    get_all_carts,
    get_cart_by_id,
    create_cart,
    update_cart,
    delete_cart,
    get_all_carts_collection
)
from src.swagger.carts_swagger import (
    DELETE_CARTS,
    GET_CARTS,
    GET_CARTS_BY_ID,
    UPDATE_CARTS,
    CREATE_CARTS
)

carts_bp = Blueprint('carts', __name__)

@carts_bp.route('/carts/collections', methods=['GET'])
def cart_route_get_collections():
    return get_all_carts_collection()

@carts_bp.route('/carts', methods=['GET'])
@swag_from(GET_CARTS)
def cart_route_get_all():
    return get_all_carts()

   
@carts_bp.route('/carts', methods=['POST'])
@swag_from(CREATE_CARTS)
# def cart_route_post():
#     data = request.get_json()
#     product_id = data.get('product_id')
#     user_id = data.get('user_id')
#     quantity = data.get('quantity')
#     user_address = data.get('user_address')
#     total_price = data.get('total_price')

#     return create_cart(product_id=product_id, user_id=user_id, quantity=quantity, user_address=user_address, total_price=total_price)
def cart_route_post():
    try:
        # Parse the incoming JSON body
        data = request.get_json()

        # Ensure data is an array
        if not isinstance(data, list):
            return jsonify({"error": "Expected a list of cart items"}), 400

        # Process each cart item in the array
        results = []
        for item in data:
            product_id = item.get('product_id')
            user_id = item.get('user_id')
            quantity = item.get('quantity')
            user_address = item.get('user_address')
            total_price = item.get('total_price')

            # Validate required fields
            if not all([product_id, user_id, quantity, user_address, total_price]):
                return jsonify({"error": "Missing required fields in cart item"}), 400

            # Create each cart item
            result = create_cart(
                user_id=user_id,
                product_id=product_id,
                quantity=quantity,
                total_price=total_price,
                user_address=user_address
            )

            # If there was an error creating this cart item, add the error to results
            if isinstance(result, tuple) and result[1] != 201:
                results.append({"error": result[0].json["error"]})
            else:
                results.append(result)

        # Return results
        return jsonify({
            "message": "Cart items processed",
            "results": results
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

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