GET_ALL_TRANSACTIONS = {
    'tags': ['Transactions'],
    'summary': 'Retrieve all transactions for the authenticated user',
    'description': 'Fetch a list of all transactions for the currently authenticated user.',
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
            'description': 'List of all transactions for the user',
            'content': {
                'application/json': {
                    'example': {
                        'transactions': [
                            {
                                'checkout_id': 'chk_12345',
                                'total_price': 150.00,
                                'status': 'completed',
                                'created_at': '2024-12-19T12:00:00+00:00'
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

GET_TRANSACTION_BY_ID = {
    'tags': ['Transactions'],
    'summary': 'Retrieve a transaction by its checkout ID',
    'description': 'Fetch details of a specific transaction for the authenticated user based on its checkout ID.',
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
            'name': 'checkout_id',
            'in': 'path',
            'required': True,
            'description': 'The ID of the checkout to fetch',
            'schema': {
                'type': 'string'
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Details of the transaction',
            'content': {
                'application/json': {
                    'example': {
                        'checkout_id': 'chk_12345',
                        'user_id': 1,
                        'total_price': 150.00,
                        'status': 'completed',
                        'items': [
                            {
                                'product_id': 1,
                                'quantity': 2,
                                'price': 50.00
                            },
                            {
                                'product_id': 2,
                                'quantity': 1,
                                'price': 50.00
                            }
                        ],
                        'created_at': '2024-12-19T12:00:00+00:00'
                    }
                }
            }
        },
        401: {
            'description': 'Unauthorized'
        },
        404: {
            'description': 'Transaction not found'
        },
        500: {
            'description': 'Internal server error'
        }
    }
}

DELETE_TRANSACTION = {
    'tags': ['Transactions'],
    'summary': 'Delete a transaction by its checkout ID',
    'description': 'Delete a specific transaction for the authenticated user based on its checkout ID.',
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
            'name': 'checkout_id',
            'in': 'path',
            'required': True,
            'description': 'The ID of the checkout to delete',
            'schema': {
                'type': 'string'
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Transaction deleted successfully',
            'content': {
                'application/json': {
                    'example': {
                        'message': 'Transaction deleted successfully'
                    }
                }
            }
        },
        401: {
            'description': 'Unauthorized'
        },
        404: {
            'description': 'Transaction not found'
        },
        500: {
            'description': 'Internal server error'
        }
    }
}
GET_ALL_TRANSACTIONS_BY_SELLER = {
    'tags': ['Transactions'],
    'summary': 'Retrieve transaction statistics for a seller',
    'description': 'Fetches total transactions, products listed, and products sold for a seller based on the authenticated user.',
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
            'description': 'Transaction statistics for the seller',
            'content': {
                'application/json': {
                    'example': {
                        'total_transactions': 25,
                        'product_listed': 10,
                        'products_sold': 100
                    }
                }
            }
        },
        404: {
            'description': 'Seller not found',
            'content': {
                'application/json': {
                    'example': {
                        'error': 'Seller not found'
                    }
                }
            }
        },
        500: {
            'description': 'Internal server error'
        }
    }
}