GET_ALL_REVIEWS = {
    'tags': ['Reviews'],
    'summary': 'Retrieve all reviews',
    'description': 'Fetch a list of all reviews.',
    'responses': {
        200: {
            'description': 'List of all reviews',
            'content': {
                'application/json': {
                    'example': {
                        'reviews': [
                            {
                                'review_id': 1,
                                'user_id': 2,
                                'product_id': 5,
                                'rating': 4,
                                'review': 'Great product!',
                                'created_at': '2024-12-19T12:00:00+00:00'
                            }
                        ]
                    }
                }
            }
        },
        500: {
            'description': 'Internal server error'
        }
    }
}

GET_REVIEWS_BY_PRODUCT_ID = {
    'tags': ['Reviews'],
    'summary': 'Retrieve reviews by product ID',
    'description': 'Fetch a list of reviews for a specific product.',
    'parameters': [
        {
            'name': 'product_id',
            'in': 'path',
            'required': True,
            'description': 'The ID of the product to fetch reviews for',
            'schema': {
                'type': 'integer'
            }
        }
    ],
    'responses': {
        200: {
            'description': 'List of reviews for the product',
            'content': {
                'application/json': {
                    'example': {
                        'reviews': [
                            {
                                'review_id': 1,
                                'user_id': 2,
                                'product_id': 5,
                                'rating': 4,
                                'review': 'Great product!',
                                'created_at': '2024-12-19T12:00:00+00:00'
                            }
                        ]
                    }
                }
            }
        },
        404: {
            'description': 'Product not found'
        },
        500: {
            'description': 'Internal server error'
        }
    }
}

ADD_REVIEW = {
    'tags': ['Reviews'],
    'summary': 'Add a new review',
    'description': 'Allows an authenticated user to add a review for a product.',
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
            'description': 'The details of the review to add.',
            'schema': {
                'type': 'object',
                'properties': {
                    'product_id': {
                        'type': 'integer',
                        'description': 'The ID of the product being reviewed.'
                    },
                    'rating': {
                        'type': 'integer',
                        'description': 'Rating for the product (1-5).'
                    },
                    'review': {
                        'type': 'string',
                        'description': 'The review text.'
                    }
                },
                'required': ['product_id', 'rating', 'review']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Review added successfully',
            'content': {
                'application/json': {
                    'example': {
                        'message': 'Review added successfully'
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

EDIT_REVIEW = {
    'tags': ['Reviews'],
    'summary': 'Edit an existing review',
    'description': 'Allows an authenticated user to edit their review.',
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
            'name': 'review_id',
            'in': 'path',
            'required': True,
            'description': 'The ID of the review to edit',
            'schema': {
                'type': 'integer'
            }
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'The updated details of the review.',
            'schema': {
                'type': 'object',
                'properties': {
                    'rating': {
                        'type': 'integer',
                        'description': 'Updated rating for the product (1-5).'
                    },
                    'review': {
                        'type': 'string',
                        'description': 'Updated review text.'
                    }
                },
                'required': ['rating', 'review']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Review updated successfully',
            'content': {
                'application/json': {
                    'example': {
                        'message': 'Review updated successfully'
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
            'description': 'Review not found'
        },
        500: {
            'description': 'Internal server error'
        }
    }
}

DELETE_REVIEW = {
    'tags': ['Reviews'],
    'summary': 'Delete a review',
    'description': 'Allows an authenticated user to delete their review.',
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
            'name': 'review_id',
            'in': 'path',
            'required': True,
            'description': 'The ID of the review to delete',
            'schema': {
                'type': 'integer'
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Review deleted successfully',
            'content': {
                'application/json': {
                    'example': {
                        'message': 'Review deleted successfully'
                    }
                }
            }
        },
        401: {
            'description': 'Unauthorized'
        },
        404: {
            'description': 'Review not found'
        },
        500: {
            'description': 'Internal server error'
        }
    }
}