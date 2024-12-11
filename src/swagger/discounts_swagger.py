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
