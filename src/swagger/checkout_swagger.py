CHECKOUT = {
    'tags': ['Checkout'],
    'summary': 'Checkout items in the cart',
    'description': 'Allows a user to checkout items from their cart with a selected payment method. The system processes the items, groups them by seller, calculates total price, reduces stock, and creates orders.',
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
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'Details of the cart items to checkout, including payment method.',
            'schema': {
                'type': 'object',
                'properties': {
                    'cart_items': {
                        'type': 'array',
                        'description': 'A list of cart items to checkout.',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'product_id': {
                                    'type': 'integer',
                                    'description': 'ID of the product'
                                },
                                'quantity': {
                                    'type': 'integer',
                                    'description': 'Quantity of the product to purchase'
                                }
                            },
                            'required': ['product_id', 'quantity']
                        }
                    },
                    'payment_method': {
                        'type': 'string',
                        'description': 'The selected payment method (e.g., credit_card, cash).'
                    }
                },
                'required': ['cart_items', 'payment_method']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Checkout completed successfully',
            'content': {
                'application/json': {
                    'example': {
                        'message': 'Checkout successful',
                        'orders': [
                            {
                                'order_id': 12345,
                                'total_price': 150.00,
                                'status': 'paid'
                            },
                            {
                                'order_id': 12346,
                                'total_price': 200.00,
                                'status': 'paid'
                            }
                        ]
                    }
                }
            }
        },
        400: {
            'description': 'Not enough stock for one or more products or invalid input',
            'content': {
                'application/json': {
                    'example': {
                        'error': 'Not enough stock for Laptop'
                    }
                }
            }
        },
        404: {
            'description': 'User not found',
            'content': {
                'application/json': {
                    'example': {
                        'error': 'User not found'
                    }
                }
            }
        },
        500: {
            'description': 'Internal server error'
        }
    }
}
CHECKOUT_NOW = {
    'tags': ['Checkout'],
    'summary': 'Checkout Items',
    'description': 'Create Checkout Transaction',
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
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'Create a checkout transaction',
            'schema': {
                'type': 'object',
                'properties': {                   
                    'checkout_id': {
                        'type': 'string'
                    },
                    'total_price': {
                        'type': 'number',
                        'format': 'float'
                    },
                    'payment_method': {
                        'type': 'string'
                    },
                },
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Checkout completed successfully',
            'content': {
                'application/json': {
                    'example': {
                        'message': 'Checkout successful',
                        'orders': [
                            {
                                'order_id': 12345,
                                'total_price': 150.00,
                                'status': 'paid'
                            },
                            {
                                'order_id': 12346,
                                'total_price': 200.00,
                                'status': 'paid'
                            }
                        ]
                    }
                }
            }
        },
        400: {
            'description': 'Not enough stock for one or more products or invalid input',
            'content': {
                'application/json': {
                    'example': {
                        'error': 'Not enough stock for Laptop'
                    }
                }
            }
        },
        404: {
            'description': 'User not found',
            'content': {
                'application/json': {
                    'example': {
                        'error': 'User not found'
                    }
                }
            }
        },
        500: {
            'description': 'Internal server error'
        }
    }
}

CHECKOUT_ITEM = {
    'tags': ['Checkout'],
    'summary': 'Create new checkout items',
    'description': 'Add multiple items to the database.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'Array of order items to be created.',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'product_id': {
                            'type': 'integer',
                            'description': 'ID of the product'
                        },
                        'user_id': {
                            'type': 'integer',
                            'description': 'ID of the user'
                        },
                        'quantity': {
                            'type': 'number',
                            'description': 'Quantity of the product'
                        },
                        'user_address': {
                            'type': 'string',
                            'description': 'Address of the user'
                        },
                        'total_price': {
                            'type': 'number',
                            'format': 'float',
                            'description': 'Total price for the product quantity'
                        },
                        'checkout_order_id': {
                            'type': 'string',
                           
                        },
                    },
                    'required': ['product_id', 'user_id', 'quantity', 'user_address', 'total_price', 'checkout_order_id']
                }
            }
        }
    ],
    'requestBody': {
        'content': {
            'application/json': {
                'example': [
                    {
                        'product_id': 101,
                        'user_id': 10,
                        'quantity': 2,
                        'user_address': '123 Main Street',
                        'total_price': 200.00
                    },
                    {
                        'product_id': 102,
                        'user_id': 10,
                        'quantity': 1,
                        'user_address': '123 Main Street',
                        'total_price': 100.00
                    }
                ]
            }
        }
    },
    'responses': {
        201: {
            'description': 'Cart items created successfully',
        },
        400: {
            'description': 'Invalid input or missing fields in one or more items'
        },
        500: {
            'description': 'Internal server error'
        }
    }
}