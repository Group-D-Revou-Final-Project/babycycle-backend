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
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'Create a new product',
            'schema': {
                'type': 'object',
                'properties': {
                    'user_id': {
                        'type': 'integer'
                    },
                    'name': {
                        'type': 'string'
                    },
                    'price': {
                        'type': 'number'
                    },
                    'category': {
                        'type': 'string'
                    },
                    'descriptions': {
                        'type': 'string'
                    },
                    'is_warranty': {
                        'type': 'boolean'
                    },
                    'image_url': {
                        'type': 'string'
                    },
                    'stock': {
                        'type': 'integer'
                    },
                },
            }
        }
    ],
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
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'The updated product details',
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {
                        'type': 'string'
                    },
                    'price': {
                        'type': 'number'
                    },
                    'category': {
                        'type': 'string'
                    },
                    'descriptions': {
                        'type': 'string'
                    },
                    'image_url': {
                        'type': 'string'
                    },
                    'stock': {
                        'type': 'integer'
                    },
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
                        'name': {
                            'type': 'string',
                            'example': 'Laptop'
                        },
                        'price': {
                            'type': 'number',
                            'format': 'float',
                            'example': 1100.00
                        },
                        'description': {
                            'type': 'string',
                            'example': 'A powerful laptop with a discount'
                        },
                        'category': {
                            'type': 'string',
                            'example': 'Electronics'
                        },
                        'stock': {
                            'type': 'integer',
                            'example': 4
                        },
                        'is_warranty': {
                            'type': 'boolean',
                            'example': True
                        },
                        'image_url': {
                            'type': 'string',
                            'example': 'http://example.com/laptop.jpg'
                        }
                    },
                    'required': ['name', 'price', 'category']  # Required fields
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
GET_PRODUCTS_BY_SORTING = {
    'tags': ['Products'],
    'summary': 'Retrieve products with sorting, pagination, and filtering',
    'description': 'Fetch a list of products sorted by a specified field with pagination.',
    'parameters': [
        {
            'name': 'limit',
            'in': 'query',
            'required': False,
            'description': 'The maximum number of products to return',
            'schema': {
                'type': 'integer',
                'default': 10
            }
        },
        {
            'name': 'offset',
            'in': 'query',
            'required': False,
            'description': 'The number of products to skip before starting to collect the result set',
            'schema': {
                'type': 'integer',
                'default': 0
            }
        },
        {
            'name': 'sort_by',
            'in': 'query',
            'required': False,
            'description': 'The field to sort products by (e.g., stock, price, name)',
            'schema': {
                'type': 'string',
                'default': 'stock'
            }
        }
    ],
    'responses': {
        200: {
            'description': 'List of products sorted and paginated',
            'content': {
                'application/json': {
                    'example': {
                        'total_count': 50,
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
                            },
                            {
                                'id': 2,
                                'name': 'Smartphone',
                                'price': 800.00,
                                'description': 'A sleek smartphone',
                                'category': 'Electronics',
                                'stock': 10,
                                'is_warranty': True,
                                'image_url': 'http://example.com/smartphone.jpg',
                                'created_at': '2024-12-08T14:23:30+00:00',
                                'updated_at': '2024-12-08T14:23:30+00:00'
                            }
                        ]
                    }
                }
            }
        },
        400: {
            'description': 'Invalid query parameters'
        },
        500: {
            'description': 'Internal server error'
        }
    }
}
GET_PRODUCTS_BY_CATEGORY = {
    'tags': ['Products'],
    'summary': 'Retrieve products by category with pagination',
    'description': 'Fetch a list of products filtered by a specific category, with optional pagination.',
    'parameters': [
        {
            'name': 'limit',
            'in': 'query',
            'required': False,
            'description': 'The maximum number of products to return',
            'schema': {
                'type': 'integer',
                'default': 10
            }
        },
        {
            'name': 'offset',
            'in': 'query',
            'required': False,
            'description': 'The number of products to skip before starting to collect the result set',
            'schema': {
                'type': 'integer',
                'default': 0
            }
        },
        {
            'name': 'category',
            'in': 'query',
            'required': True,
            'description': 'The category to filter products by',
            'schema': {
                'type': 'string'
            }
        }
    ],
    'responses': {
        200: {
            'description': 'List of products filtered by category and paginated',
            'content': {
                'application/json': {
                    'example': {
                        'total_count': 20,
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
                            },
                            {
                                'id': 2,
                                'name': 'Smartphone',
                                'price': 800.00,
                                'description': 'A sleek smartphone',
                                'category': 'Electronics',
                                'stock': 10,
                                'is_warranty': True,
                                'image_url': 'http://example.com/smartphone.jpg',
                                'created_at': '2024-12-08T14:23:30+00:00',
                                'updated_at': '2024-12-08T14:23:30+00:00'
                            }
                        ]
                    }
                }
            }
        },
        400: {
            'description': 'Invalid query parameters or missing category'
        },
        500: {
            'description': 'Internal server error'
        }
    }
}

GET_PRODUCTS_BY_WARRANTY = {
    'tags': ['Products'],
    'summary': 'Retrieve products by warranty status with pagination',
    'description': 'Fetch a list of products filtered by warranty status, with optional pagination.',
    'parameters': [
        {
            'name': 'limit',
            'in': 'query',
            'required': False,
            'description': 'The maximum number of products to return',
            'schema': {
                'type': 'integer',
                'default': 10
            }
        },
        {
            'name': 'offset',
            'in': 'query',
            'required': False,
            'description': 'The number of products to skip before starting to collect the result set',
            'schema': {
                'type': 'integer',
                'default': 0
            }
        },
        {
            'name': 'is_warranty',
            'in': 'query',
            'required': False,
            'description': 'Filter products by warranty status (true or false)',
            'schema': {
                'type': 'boolean',
                'default': True
            }
        }
    ],
    'responses': {
        200: {
            'description': 'List of products filtered by warranty status and paginated',
            'content': {
                'application/json': {
                    'example': {
                        'total_count': 15,
                        'products': [
                            {
                                'id': 1,
                                'name': 'Laptop',
                                'price': 1200.00,
                                'description': 'A powerful laptop with warranty',
                                'category': 'Electronics',
                                'stock': 5,
                                'is_warranty': True,
                                'image_url': 'http://example.com/laptop.jpg',
                                'created_at': '2024-12-08T14:23:30+00:00',
                                'updated_at': '2024-12-08T14:23:30+00:00'
                            },
                            {
                                'id': 2,
                                'name': 'Smartphone',
                                'price': 800.00,
                                'description': 'A sleek smartphone with warranty',
                                'category': 'Electronics',
                                'stock': 10,
                                'is_warranty': True,
                                'image_url': 'http://example.com/smartphone.jpg',
                                'created_at': '2024-12-08T14:23:30+00:00',
                                'updated_at': '2024-12-08T14:23:30+00:00'
                            }
                        ]
                    }
                }
            }
        },
        400: {
            'description': 'Invalid query parameters'
        },
        500: {
            'description': 'Internal server error'
        }
    }
}
