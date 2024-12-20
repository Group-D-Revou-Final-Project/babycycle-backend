GET_ALL_SELLERS = {
    'tags': ['Sellers'],
    'summary': 'Retrieve all sellers',
    'description': 'Fetch a list of all registered sellers.',
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
    'responses': {
        200: {
            'description': 'List of all sellers',
            'content': {
                'application/json': {
                    'example': {
                        'sellers': [
                            {
                                'seller_id': 1,
                                'name': 'Seller A',
                                'address': '123 Main St',
                                'contact': '1234567890'
                            }
                        ]
                    }
                }
            }
        },
        401: {
            'description': 'Unauthorized'
        },
        500: {
            'description': 'Internal server error'
        }
    }
}

GET_SELLER_BY_ID = {
    'tags': ['Sellers'],
    'summary': 'Retrieve a seller by ID',
    'description': 'Fetch details of a specific seller using their seller ID.',
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
            'name': 'seller_id',
            'in': 'path',
            'required': True,
            'description': 'The ID of the seller to fetch',
            'schema': {
                'type': 'integer'
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Details of the seller',
            'content': {
                'application/json': {
                    'example': {
                        'seller_id': 1,
                        'name': 'Seller A',
                        'address': '123 Main St',
                        'contact': '1234567890'
                    }
                }
            }
        },
        401: {
            'description': 'Unauthorized'
        },
        404: {
            'description': 'Seller not found'
        },
        500: {
            'description': 'Internal server error'
        }
    }
}

CREATE_SELLER = {
    'tags': ['Sellers'],
    'summary': 'Create a new seller',
    'description': 'Allows an authenticated user to create a new seller profile.',
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
            'description': 'Details of the seller to create.',
            'schema': {
                'type': 'object',
                'properties': {
                    'user_id': {
                        'type': 'integer',
                        'description': 'The ID of the user creating the seller profile.'
                    },
                    'name': {
                        'type': 'string',
                        'description': 'The name of the seller.'
                    },
                    'address': {
                        'type': 'string',
                        'description': 'The address of the seller.'
                    },
                    'contact': {
                        'type': 'string',
                        'description': 'The contact information for the seller.'
                    }
                },
                'required': ['user_id', 'name', 'address', 'contact']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Seller created successfully',
            'content': {
                'application/json': {
                    'example': {
                        'message': 'Seller created successfully'
                    }
                }
            }
        },
        400: {
            'description': 'Invalid input data'
        },
        401: {
            'description': 'Unauthorized'
        },
        500: {
            'description': 'Internal server error'
        }
    }
}

UPDATE_SELLER = {
    'tags': ['Sellers'],
    'summary': 'Update a seller profile',
    'description': 'Allows an authenticated user to update details of a seller profile.',
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
            'name': 'seller_id',
            'in': 'path',
            'required': True,
            'description': 'The ID of the seller to update',
            'schema': {
                'type': 'integer'
            }
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'Updated details of the seller.',
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {
                        'type': 'string',
                        'description': 'Updated name of the seller.'
                    },
                    'address': {
                        'type': 'string',
                        'description': 'Updated address of the seller.'
                    },
                    'contact': {
                        'type': 'string',
                        'description': 'Updated contact information for the seller.'
                    }
                },
                'required': ['name', 'address', 'contact']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Seller updated successfully',
            'content': {
                'application/json': {
                    'example': {
                        'message': 'Seller updated successfully'
                    }
                }
            }
        },
        400: {
            'description': 'Invalid input data'
        },
        401: {
            'description': 'Unauthorized'
        },
        404: {
            'description': 'Seller not found'
        },
        500: {
            'description': 'Internal server error'
        }
    }
}

DELETE_SELLER = {
    'tags': ['Sellers'],
    'summary': 'Delete a seller profile',
    'description': 'Allows an authenticated user to delete a seller profile.',
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
            'name': 'seller_id',
            'in': 'path',
            'required': True,
            'description': 'The ID of the seller to delete',
            'schema': {
                'type': 'integer'
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Seller deleted successfully',
            'content': {
                'application/json': {
                    'example': {
                        'message': 'Seller deleted successfully'
                    }
                }
            }
        },
        401: {
            'description': 'Unauthorized'
        },
        404: {
            'description': 'Seller not found'
        },
        500: {
            'description': 'Internal server error'
        }
    }
}

GET_PRODUCTS_BY_SELLER = {
    'tags': ['Sellers'],
    'summary': 'Retrieve products by seller',
    'description': 'Fetch a list of products associated with the authenticated seller.',
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
    'responses': {
        200: {
            'description': 'List of products associated with the seller',
            'content': {
                'application/json': {
                    'example': {
                        'products': [
                            {
                                'product_id': 1,
                                'name': 'Product A',
                                'price': 100.00,
                                'stock': 10,
                                'category': 'Category A'
                            },
                            {
                                'product_id': 2,
                                'name': 'Product B',
                                'price': 200.00,
                                'stock': 5,
                                'category': 'Category B'
                            }
                        ]
                    }
                }
            }
        },
        401: {
            'description': 'Unauthorized'
        },
        500: {
            'description': 'Internal server error'
        }
    }
}