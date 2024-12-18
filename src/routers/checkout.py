from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.models.users_model import UserModel
from flasgger import swag_from

from src.services.checkout_service import (
    checkout_now,
    checkout_item_now,
    create_order_items
)
from src.swagger.checkout_swagger import (
    CHECKOUT,
    CHECKOUT_NOW,
    CHECKOUT_ITEM
)


checkout_bp=Blueprint('checkout', __name__)
@checkout_bp.route('/checkout', methods=['POST'])
@jwt_required()
@swag_from(CHECKOUT)
def checkout():
    current_user_id = get_jwt_identity()  
    data = request.json
    cart_items = data.get('cart_items')
    payment_method = data.get('payment_method')

    user = UserModel.query.get(current_user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return checkout_now(cart_items=cart_items, payment_method=payment_method, current_user_id=current_user_id)


@checkout_bp.route('/checkout/now', methods=['POST'])
@jwt_required()
@swag_from(CHECKOUT_NOW)
def checkout_now_route():
    current_user_id = get_jwt_identity()
    data = request.get_json()
    # total_price = data.get('total_price')
    payment_method = data.get('payment_method')
    checkout_id = data.get('checkout_id')

    return checkout_item_now(checkout_id=checkout_id, payment_method=payment_method, current_user_id=current_user_id)

@checkout_bp.route('/checkout/items', methods=['POST'])
@jwt_required()
@swag_from(CHECKOUT_ITEM)
def checkout_items():
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
            checkout_order_id = item.get('checkout_order_id')
            quantity = item.get('quantity')
            user_address = item.get('user_address')
            total_price = item.get('total_price')

            # Validate required fields
            if not all([product_id, checkout_order_id, quantity, user_address, total_price]):
                results.append({"error": "Missing required fields in order item", "item": item})
                continue

            # Create or update each order item
            response, status_code = create_order_items(
                user_id=userID,
                product_id=product_id,
                quantity=quantity,
                total_price=total_price,
                user_address=user_address,
                checkout_order_id=checkout_order_id
            )

            # Append response to results
            if status_code == 201 or status_code == 200:
                results.append(response)
            else:
                results.append({"error": response.get("error", "Unknown error"), "item": item})

        # Return the results
        return jsonify({
            "message": "Order items processed",
            "results": results
        }), status_code
    except Exception as e:
        return jsonify({"error": f"An error occurred route: {str(e)}"}), 500

