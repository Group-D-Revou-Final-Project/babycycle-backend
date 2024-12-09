from flask import jsonify
from src.models.products_model import ProductModel
from src.models.discounts_model import DiscountModel

from src.config.settings import db


def get_all_products():
    # Query all products
    products = ProductModel.query.filter_by(is_deleted=False).all()
    
    # Count the total number of products
    total_count = ProductModel.query.count()
    
    # Return the total count and the list of products
    return jsonify({
        "total_count": total_count,
        "products": [product.to_dict() for product in products]
    }), 200

def get_product_by_id(product_id):
    product = ProductModel.query.filter_by(id=product_id, is_deleted=False).first()
    if product:
        return jsonify(product.to_dict()), 200
    else:
        return jsonify({"error": "Product not found"}), 404
    

def create_product(name, price, description, category, is_warranty, image_url, stock):
    try:
        # Create a new ProductModel instance
        new_product = ProductModel(
            name=name,
            price=price,
            description=description,
            category=category,
            is_warranty=is_warranty,
            image_url=image_url,
            stock=stock
        )
        
        # Add to database
        db.session.add(new_product)
        db.session.commit()
        
        # Return the created product
        return jsonify(new_product.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

def update_product(product_id, name, price, descriptions, category, is_warranty, image_url, stock):
    product = ProductModel.query.filter_by(id=product_id, is_deleted=False).first()
    if product:
        try:
            product.name = name
            product.price = price
            product.descriptions = descriptions
            product.category = category
            product.is_warranty = is_warranty
            product.image_url = image_url
            product.stock = stock
            db.session.commit()
            return jsonify(product.to_dict()), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Product not found"}), 404
    
def delete_product(product_id):
    product = ProductModel.query.filter_by(id=product_id, is_deleted=False).first()
    if product:
        try:
            product.is_deleted = True
            db.session.commit()
            return jsonify({"message": "Product deleted successfully"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Product not found"}), 404
    
def deactivate_product(product_id):
    product = ProductModel.query.filter_by(id=product_id, is_deleted=False).first()
    if product:
        try:
            product.is_deactivated = True
            db.session.commit()
            return jsonify({"message": "Product deactivated successfully"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Product not found"}), 404