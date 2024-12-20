CREATE_CARTS = {
    'tags': ['Carts'],
    'summary': 'Create new carts',
    'description': 'Add multiple cart items to the database.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'Array of cart items to be created.',
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
                    },
                    'required': ['product_id', 'user_id', 'quantity', 'user_address', 'total_price']
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


GET_CARTS = {
    'tags': ['Carts'],
    'responses': {
        200: {
            'description': 'List of all carts',
            'content': {
                'application/json': {
                    'example': {
                        'carts': [
                            {
                                'id': 1,
                                'product_id': 101,
                                'user_id': 10,
                                'quantity': 2,
                                'user_address': '123 Main Street',
                                'total_price': 200.00,
                            }
                        ]
                    }
                }
            }
        },
        500: {
            'description': 'Internal server error'
        }
    },
    'parameters': [],
    'description': 'Retrieve all carts or create a new cart',
    'requestBody': {
        'content': {
            'application/json': {
                'example': {
                    'product_id': 101,
                    'user_id': 10,
                    'quantity': 2,
                    'user_address': '123 Main Street',
                    'total_price': 200.00
                }
            }
        },
        'required': True
    }
}
GET_CARTS_BY_ID = {
    'tags': ['Carts'],
    'summary': 'Retrieve a carts by ID',
    'description': 'Fetch details of a product by its ID.',
    'parameters': [
        {
            'name': 'cart_id',
            'in': 'path',
            'required': True,
            'description': 'The ID of the cart',
            'schema': {
                'type': 'integer'
            }
        }
    ],
    'responses': {
        200: {
            'description': 'cart details',
            'content': {
                'application/json': {
                    'example': {
                        'id': 1,
                        'product_id': 2,
                        'user_id': 3,
                        'quantity': 4,
                        'user_address': '123 Main Street',
                        'total_price': 200.00
                    }
                }
            }
        },
        404: {
            'description': 'Cart not found'
        }
    }
}

UPDATE_CARTS = {
    'tags': ['Carts'],
    'summary': 'Update a Carts',
    'description': 'Update an existing carts by its ID.',
    'parameters': [
        {
            'name': 'cart_id',
            'in': 'path',
            'required': True,
            'description': 'The ID of the carts to update',
            'schema': {
                'type': 'integer'
            }
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'The updated carts details',
            'schema': {
                'type': 'object',
                'properties': {
                    'quantity': {
                        'type': 'number'
                    },
                    'total_price': {
                        'type': 'number',
                        'format': 'float'
                    }
                },
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
                        'quantity': {
                            'type': 'number',
                            'example': 3
                        },
                        'total_price': {
                            'type': 'number',
                            'format': 'float',
                            'example': 11000.00
                        },  
                    },
                    'required': ['quantity', 'total_price']
                }
            }
        }
    },
    'responses': {
        200: {
            'description': 'Carts updated successfully',
        },
        400: {
            'description': 'Invalid input'
        },
        404: {
            'description': 'Product not found'
        }
    }
}

DELETE_CARTS = {
    'tags': ['Carts'],
    'summary': 'Delete a cart',
    'description': 'Remove a cart by its ID.',
    'parameters': [
        {
            'name': 'cart_id',
            'in': 'path',
            'required': True,
            'description': 'The ID of the cart to delete',
            'schema': {
                'type': 'integer'
            }
        }
    ],
    'responses': {
        204: {
            'description': 'Cart deleted successfully'
        },
        404: {
            'description': 'Cart not found'
        }
    }}