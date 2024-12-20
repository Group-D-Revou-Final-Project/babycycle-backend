GET_DISCOUNT_BY_ID = {
    'tags': ['Discounts'],
    'summary': 'Retrieve the active discount for a product by product ID',
    'description': 'Fetch the discount details for a specific product if the discount is active.',
    'parameters': [
        {
            'name': 'product_id',
            'in': 'path',
            'required': True,
            'description': 'The ID of the product to fetch the discount for',
            'schema': {
                'type': 'integer'
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Discount found for the product',
            'content': {
                'application/json': {
                    'example': {
                        'product_id': 101,
                        'discount_percentage': 10,
                        'is_active': True
                    }
                }
            }
        },
        404: {
            'description': 'Discount not found for the specified product'
        },
        500: {
            'description': 'Internal server error'
        }
    }
}

GET_CALCULATED_DISCOUNT = {
    'tags': ['Discounts'],
    'summary': 'Retrieve the calculated discounted price for a product by product ID',
    'description': 'Fetch the calculated discounted price for a specific product based on the active discount.',
    'parameters': [
        {
            'name': 'product_id',
            'in': 'path',
            'required': True,
            'description': 'The ID of the product to calculate the discount for',
            'schema': {
                'type': 'integer'
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Calculated discounted price for the product',
            'content': {
                'application/json': {
                    'example': {
                        'discounted_price': 900.00
                    }
                }
            }
        },
        404: {
            'description': 'Product or discount not found'
        },
        500: {
            'description': 'Internal server error'
        }
    }
}
CREATE_DISCOUNT = {
    'tags': ['Discounts'],
    'summary': 'Create a new discount',
    'description': 'Allows the creation of a discount for a specific product.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'description': 'Details of the discount to create.',
            'schema': {
                'type': 'object',
                'properties': {
                    'product_id': {
                        'type': 'integer',
                        'description': 'The ID of the product the discount applies to.',
                        'example': 1
                    },
                    'discount_percentage': {
                        'type': 'number',
                        'format': 'float',
                        'description': 'The percentage of the discount.',
                        'example': 15.5
                    },
                    'start_date': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'The start date of the discount.',
                        'example': '2024-01-01T00:00:00Z'
                    },
                    'end_date': {
                        'type': 'string',
                        'format': 'date-time',
                        'description': 'The end date of the discount.',
                        'example': '2024-01-15T23:59:59Z'
                    },
                    'is_active': {
                        'type': 'boolean',
                        'description': 'Indicates if the discount is active.',
                        'example': True
                    }
                },
                'required': ['product_id', 'discount_percentage', 'start_date', 'end_date', 'is_active']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Discount created successfully',
            'content': {
                'application/json': {
                    'example': {
                        'message': 'Discount created successfully',
                        'discount_id': 12345
                    }
                }
            }
        },
        400: {
            'description': 'Invalid input data',
            'content': {
                'application/json': {
                    'example': {
                        'error': 'Invalid product ID or missing required fields.'
                    }
                }
            }
        },
        500: {
            'description': 'Internal server error'
        }
    }
}
