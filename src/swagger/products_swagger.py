GET_ALL_PRODUCTS = {
    'tags': ['Products'],
    'summary': 'Retrieve all products',
    'description': 'Fetch a list of all products.',
    'responses': {
        200: {
            'description': 'List of products',
            'content': {
                'application/json': {
                    'example': {
                        'total_count': 2,
                        'products': [
                            {
                                'id': 1,
                                'name': 'Laptop',
                                'price': 1200.00,
                                'description': 'A powerful laptop',
                                'category': 'Electronics',
                                'stock': 5,
                                'is_warranty': True,
                                'image_url': 'http://example.com/laptop.jpg',
                                'created_at': '2024-12-08T14:23:30+00:00',
                                'updated_at': '2024-12-08T14:23:30+00:00'
                            }
                        ]
                    }
                }
            }
        }
    }
}

GET_PRODUCT_BY_ID = {
    'tags': ['Products'],
    'summary': 'Retrieve a product by ID',
    'description': 'Fetch details of a product by its ID.',
    'parameters': [
        {
            'name': 'product_id',
            'in': 'path',
            'required': True,
            'description': 'The ID of the product',
            'schema': {
                'type': 'integer'
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Product details',
            'content': {
                'application/json': {
                    'example': {
                        'id': 1,
                        'name': 'Laptop',
                        'price': 1200.00,
                        'description': 'A powerful laptop',
                        'category': 'Electronics',
                        'stock': 5,
                        'is_warranty': True,
                        'image_url': 'http://example.com/laptop.jpg',
                        'created_at': '2024-12-08T14:23:30+00:00',
                        'updated_at': '2024-12-08T14:23:30+00:00'
                    }
                }
            }
        },
        404: {
            'description': 'Product not found'
        }
    }
}

CREATE_PRODUCT = {
    'tags': ['Products'],
    'summary': 'Create a new product',
    'description': 'Add a new product to the catalog.',
    'requestBody': {
        'content': {
            'application/json': {
                'example': {
                    'name': 'Laptop',
                    'price': 1200.00,
                    'description': 'A powerful laptop',
                    'category': 'Electronics',
                    'stock': 5,
                    'is_warranty': True,
                    'image_url': 'http://example.com/laptop.jpg'
                }
            }
        }
    },
    'responses': {
        201: {
            'description': 'Product created successfully',
        },
        400: {
            'description': 'Invalid input'
        }
    }
}

UPDATE_PRODUCT = {
    'tags': ['Products'],
    'summary': 'Update a product',
    'description': 'Update an existing product by its ID.',
    'parameters': [
        {
            'name': 'product_id',
            'in': 'path',
            'required': True,
            'description': 'The ID of the product to update',
            'schema': {
                'type': 'integer'
            }
        }
    ],
    'requestBody': {
        'content': {
            'application/json': {
                'example': {
                    'name': 'Laptop',
                    'price': 1100.00,
                    'description': 'A powerful laptop with a discount',
                    'category': 'Electronics',
                    'stock': 4,
                    'is_warranty': True,
                    'image_url': 'http://example.com/laptop.jpg'
                }
            }
        }
    },
    'responses': {
        200: {
            'description': 'Product updated successfully',
        },
        400: {
            'description': 'Invalid input'
        },
        404: {
            'description': 'Product not found'
        }
    }
}

DELETE_PRODUCT = {
    'tags': ['Products'],
    'summary': 'Delete a product',
    'description': 'Remove a product by its ID.',
    'parameters': [
        {
            'name': 'product_id',
            'in': 'path',
            'required': True,
            'description': 'The ID of the product to delete',
            'schema': {
                'type': 'integer'
            }
        }
    ],
    'responses': {
        204: {
            'description': 'Product deleted successfully'
        },
        404: {
            'description': 'Product not found'
        }
    }
}

DEACTIVATE_PRODUCT = {
    'tags': ['Products'],
    'summary': 'Deactivate a product',
    'description': 'Deactivate a product by its ID.',
    'parameters': [
        {
            'name': 'product_id',
            'in': 'path',
            'required': True,
            'description': 'The ID of the product to deactivate',
            'schema': {
                'type': 'integer'
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Product deactivated successfully'
        },
        404: {
            'description': 'Product not found'
        }
    }
}
