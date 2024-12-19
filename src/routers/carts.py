from flask import Blueprint, request, jsonify
from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity

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
@jwt_required()
def cart_route_get_all():
    userID = get_jwt_identity()
    return get_all_carts(user_id=userID)

   
@carts_bp.route('/carts', methods=['POST'])
@jwt_required()
@swag_from(CREATE_CARTS)
def cart_route_post():
    try:
        # Parse the incoming JSON body
        data = request.get_json()
        userID = get_jwt_identity()

        # Ensure data is an array
        if not isinstance(data, list):
            return jsonify({"error": "Expected a list of cart items"}), 400

        # Process each cart item in the array
        results = []
        for item in data:
            product_id = item.get('product_id')
            user_id = userID
            quantity = item.get('quantity')
            user_address = item.get('user_address') or None
            name = item.get('name')
            total_price = item.get('total_price')

            # Validate required fields
            if not all([product_id, user_id, quantity, name, total_price]):
                results.append({"error": "Missing required fields in cart item", "item": item})
                continue

            # Create or update each cart item
            response = create_cart(
                user_id=user_id,
                product_id=product_id,
                quantity=quantity,
                total_price=total_price,
                user_address=user_address,
                name=name
            )

            # Check the response status code
            if isinstance(response, tuple):
                # Extract error message from the response if it is an error
                if response[1] != 201 and response[1] != 200:
                    error_message = response[0].json.get("error", "Unknown error")
                    results.append({"error": error_message, "item": item})
                else:
                    results.append(response[0].json)
            else:
                results.append(response)

        # Return the results
        return jsonify({
            "message": "Cart items processed",
            "results": results
        }), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

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