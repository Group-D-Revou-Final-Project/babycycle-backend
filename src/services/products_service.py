from flask import jsonify
from src.models.products_model import ProductModel
from src.models.discounts_model import DiscountModel

from src.config.settings import db


def get_all_products():
    # Query all products
    products = ProductModel.query.all()
    
    # Count the total number of products
    total_count = ProductModel.query.count()
    
    # Return the total count and the list of products
    return jsonify({
        "total_count": total_count,
        "products": [product.to_dict() for product in products]
    }), 200

def get_product_by_id(product_id):
    product = ProductModel.query.get(product_id)
    if product:
        return jsonify(product.to_dict()), 200
    else:
        return jsonify({"error": "Product not found"}), 404
    
def create_product(name, price, description, category, is_warranty, image_url):
    try:
        # Create a new ProductModel instance
        new_product = ProductModel(
            name=name,
            price=price,
            description=description,
            category=category,
            is_warranty=is_warranty,
            image_url=image_url
        )
        
        # Add to database
        db.session.add(new_product)
        db.session.commit()
        
        # Return the created product
        return jsonify(new_product.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500