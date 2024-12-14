from flask import jsonify
from src.models.users_model import UserModel
from src.models.products_model import ProductModel
from src.models.discounts_model import DiscountModel

from src.config.settings import db


def get_all_products():
    # Query all products
    # products = ProductModel.query.filter_by(is_deleted=False).all()
    products = ProductModel.query.filter_by(is_deleted=False, is_deactivated=False).order_by(ProductModel.stock.desc()).all()
    
    # Count the total number of products
    total_count = ProductModel.query.filter_by(is_deleted=False, is_deactivated=False).count()
    
    # Return the total count and the list of products
    return jsonify({
        "total_count": total_count,
        "data": [product.to_dict() for product in products]
    }), 200

def get_all_products_limit_offset(limit, offset):
    
    if limit < 1 or offset < 0:
        return jsonify({"error": "Limit must be greater than 0 and offset must be non-negative"}), 400
    
    products = ProductModel.query.filter_by(is_deleted=False, is_deactivated=False) \
        .order_by(ProductModel.stock.desc()).limit(limit).offset(offset).all()
    
    total_count = ProductModel.query.filter_by(is_deleted=False, is_deactivated=False).count()
    
    return jsonify({
        "total_count": total_count,
        "data": [product.to_dict() for product in products]
    }), 200
    

def get_product_by_id(product_id):
    product = ProductModel.query.filter_by(id=product_id, is_deleted=False, is_deactivated=False).first()
    if product:
        return jsonify(product.to_dict()), 200
    else:
        return jsonify({"error": "Product not found"}), 404
    

def create_product(name, price, descriptions, category, is_warranty, image_url, stock):
    try:
        # Create a new ProductModel instance
        new_product = ProductModel(
            name=name,
            price=price,
            descriptions=descriptions,
            category=category,
            is_warranty=is_warranty,
            image_url=image_url,
            stock=stock,
            # user_id=user_id
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
    product = ProductModel.query.filter_by(id=product_id, is_deleted=False, is_deactivated=False).first()
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
    
def user_has_product(email):
    # Perform the query
    user_seller = UserModel.query.filter_by(email=email, is_seller=True).first()
    if user_seller is None:
        return jsonify({"error": "User Seller not found"}), 404
    result = db.session.query(
        UserModel.email,
        UserModel.username,
        ProductModel.name,
        ProductModel.user_id
    ).join(ProductModel, ProductModel.user_id == UserModel.id).filter(
        UserModel.email == email
    ).all()

    if result is None:
        return jsonify({"error": "User not found"}), 404
    
    for row in result:
        return jsonify({
            "email": row.email,
            "username": row.username,
            "product_name": row.name
        }), 200

def get_products_by_sorting(sort_by, limit, offset):

    if limit < 1 or offset < 0:
        return jsonify({"error": "Limit must be greater than 0 and offset must be non-negative"}), 400

    match sort_by:
        case "highest_price":
            products = ProductModel.query.filter_by(is_deleted=False, is_deactivated=False) \
                .order_by(ProductModel.price.desc()).limit(limit).offset(offset).all()
        case "lowest_price":  
            products = ProductModel.query.filter_by(is_deleted=False, is_deactivated=False) \
                .order_by(ProductModel.price.asc()).limit(limit).offset(offset).all()
        case "newest":
            products = ProductModel.query.filter_by(is_deleted=False, is_deactivated=False) \
                .order_by(ProductModel.created_at.desc()).limit(limit).offset(offset).all()
        case "stock":
            products = ProductModel.query.filter_by(is_deleted=False, is_deactivated=False) \
                .order_by(ProductModel.stock.desc()).limit(limit).offset(offset).all()
        case _:  
            return jsonify({"error": "Invalid sorting parameter"}), 400

    total_count = ProductModel.query.filter_by(is_deleted=False, ).count()

    return jsonify({
        "total_count": total_count,
        "data": [product.to_dict() for product in products]
    }), 200

def get_products_by_category(category, limit, offset):
    if limit < 1 or offset < 0:
        return jsonify({"error": "Limit must be greater than 0 and offset must be non-negative"}), 400
    
    match category:
        case "clothing":
            products = ProductModel.query.filter_by(is_deleted=False, is_deactivated=False, category=category) \
                .order_by(ProductModel.stock.desc()).limit(limit).offset(offset).all()
        case "furniture":  
            products = ProductModel.query.filter_by(is_deleted=False, is_deactivated=False, category=category) \
                .order_by(ProductModel.stock.asc()).limit(limit).offset(offset).all()
        case "toys":
            products = ProductModel.query.filter_by(is_deleted=False, is_deactivated=False, category=category) \
                .order_by(ProductModel.stock.desc()).limit(limit).offset(offset).all()
        case "others":
            products = ProductModel.query.filter_by(is_deleted=False, is_deactivated=False, category=category) \
                .order_by(ProductModel.stock.desc()).limit(limit).offset(offset).all()
        case _:  
            return jsonify({"error": "Available category: clothing, furniture, toys, others"}), 400

    # products = ProductModel.query.filter_by(is_deleted=False, is_deactivated=False, category=category) \
    #     .order_by(ProductModel.stock.desc()).limit(limit).offset(offset).all()

    total_count = ProductModel.query.filter_by(is_deleted=False,is_deactivated=False, category=category).count()

    return jsonify({
        "total_count": total_count,
        "data": [product.to_dict() for product in products]
    }), 200

def get_product_by_warranty(is_warranty, limit, offset):
    if limit < 1 or offset < 0:
        return jsonify({"error": "Limit must be greater than 0 and offset must be non-negative"}), 400
    
    products = ProductModel.query.filter_by(is_deleted=False, is_deactivated=False, is_warranty=is_warranty) \
        .order_by(ProductModel.stock.desc()).limit(limit).offset(offset).all()
    
    if not products:
        return jsonify({"error": "No products found"}), 404
    
    total_count = ProductModel.query.filter_by(is_deleted=False,is_deactivated=False, is_warranty=is_warranty).count()

    return jsonify({
        "total_count": total_count,
        "data": [product.to_dict() for product in products]
    }), 200