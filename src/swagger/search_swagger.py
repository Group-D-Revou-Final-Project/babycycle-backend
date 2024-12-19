SEARCH_PRODUCTS = {
    'tags': ['Search'],
    'summary': 'Search for products',
    'description': 'Allows authenticated users to search for products by a query string with optional pagination.',
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
            'name': 'query',
            'in': 'query',
            'required': True,
            'description': 'Search query string to filter products.',
            'schema': {
                'type': 'string',
                'example': 'laptop'
            }
        },
        {
            'name': 'limit',
            'in': 'query',
            'required': False,
            'description': 'The maximum number of results to return.',
            'schema': {
                'type': 'integer',
                'default': 10
            }
        },
        {
            'name': 'offset',
            'in': 'query',
            'required': False,
            'description': 'The number of results to skip before starting to collect the result set.',
            'schema': {
                'type': 'integer',
                'default': 0
            }
        }
    ],
    'responses': {
        200: {
            'description': 'List of products matching the search query',
            'content': {
                'application/json': {
                    'example': {
                        'total_count': 2,
                        'products': [
                            {
                                'id': 1,
                                'name': 'Laptop',
                                'price': 1200.00,
                                'description': 'A high-performance laptop',
                                'category': 'Electronics',
                                'stock': 5,
                                'image_url': 'http://example.com/laptop.jpg'
                            },
                            {
                                'id': 2,
                                'name': 'Laptop Bag',
                                'price': 50.00,
                                'description': 'A durable laptop bag',
                                'category': 'Accessories',
                                'stock': 15,
                                'image_url': 'http://example.com/laptop_bag.jpg'
                            }
                        ]
                    }
                }
            }
        },
        400: {
            'description': 'Invalid query parameters or missing query string'
        },
        401: {
            'description': 'Unauthorized'
        },
        500: {
            'description': 'Internal server error'
        }
    }
}
