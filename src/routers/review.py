from flask import Blueprint, request, jsonify
from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.services.review_service import (
    get_all_reviews,
    get_reviews_by_product_id,
    add_review,
    edit_review,
    delete_review
)

review_bp = Blueprint('review', __name__)

@review_bp.route('/reviews', methods=['GET'])
def review_route_get_all():
    return get_all_reviews

@review_bp.route('/reviews/<int:product_id>', methods=['GET'])
def review_route_get_by_product_id(product_id):
    return get_reviews_by_product_id(product_id)

@review_bp.route('/reviews', methods=['POST'])
@jwt_required()
def review_route_add():
    data = request.get_json()
    user_id = get_jwt_identity()
    product_id = data.get('product_id')
    rating = data.get('rating')
    review = data.get('review')

    return add_review(user_id=user_id, product_id=product_id, rating=rating, review=review)

@review_bp.route('/reviews/<int:review_id>', methods=['PUT'])
@jwt_required()
def review_route_edit(review_id):
    data = request.get_json()
    rating = data.get('rating')
    review = data.get('review')

    return edit_review(review_id=review_id, rating=rating, review=review)

@review_bp.route('/reviews/<int:review_id>', methods=['DELETE'])
@jwt_required()
def review_route_delete(review_id):
    return delete_review(review_id)