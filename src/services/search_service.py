from flask import jsonify
from src.models.products_model import ProductModel
from src.config.settings import db


def search_products(query, limit, offset):
    if limit < 1 or offset < 0:
        return jsonify({"error": "Limit must be greater than 0 and offset must be non-negative"}), 400
    
    # Perform case-insensitive search with ilike
    products = ProductModel.query.filter(ProductModel.name.ilike(f"%{query}%")) \
        .limit(limit).offset(offset).all()
    total_count = ProductModel.query.filter(ProductModel.name.ilike(f"%{query}%")).count()
   
    return jsonify({
        "total_count": total_count,
        "data": [product.to_dict() for product in products]
    }), 200