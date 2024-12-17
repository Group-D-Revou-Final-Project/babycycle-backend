CHECKOUT = {
    'tags': ['Checkout'],
    'summary': 'Checkout items in the cart',
    'description': 'Allows a user to checkout items from their cart with a selected payment method.',
    'parameters': [
        {
            'name': 'Authorization',
            'in': 'header',
            'required': True,
            'description': 'Bearer token for authentication',
            'schema': {
                'type': 'string',
                'example': 'Bearer <your-token>'
            }
        }
    ],
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': {
                    'type': 'object',
                    'properties': {
                        'cart_items': {
                            'type': 'array',
                            'description': 'A list of items in the cart to checkout',
                            'items': {
                                'type': 'object',
                                'properties': {
                                    'product_id': {'type': 'integer', 'example': 1},
                                    'quantity': {'type': 'integer', 'example': 2}
                                },
                                'required': ['product_id', 'quantity']
                            }
                        },
                        'payment_method': {
                            'type': 'string',
                            'description': 'The selected payment method (e.g., credit_card, cash)',
                            'example': 'credit_card'
                        }
                    },
                    'required': ['cart_items', 'payment_method']
                },
                'example': {
                    'cart_items': [
                        {'product_id': 1, 'quantity': 2},
                        {'product_id': 2, 'quantity': 1}
                    ],
                    'payment_method': 'credit_card'
                }
            }
        }
    },
    'responses': {
        200: {
            'description': 'Checkout completed successfully',
            'content': {
                'application/json': {
                    'example': {
                        'message': 'Checkout successful',
                        'order_id': 12345,
                        'total_price': 150.00
                    }
                }
            }
        },
        400: {
            'description': 'Invalid input data'
        },
        404: {
            'description': 'User not found'
        },
        500: {
            'description': 'Internal server error'
        }
    }
}