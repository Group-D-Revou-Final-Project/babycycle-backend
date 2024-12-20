from flask_jwt_extended import create_access_token, get_jwt_identity
from flask import jsonify
from src.models.review_model import ReviewModel
from src.models.users_model import UserModel
from src.models.products_model import ProductModel
from src.models.order_items_model import OrderItemModel
from src.config.settings import db



def add_review(user_id, product_id, rating, review):
    try:
        # Check if the user is verified
        user = UserModel.query.filter_by(id=user_id, is_verified=True).first()
        if not user:
            return jsonify({"error": "User not found or not verified"}), 404
        

        # Check if the product exists and is available
        product = ProductModel.query.filter_by(id=product_id, is_deleted=False, is_deactivated=False).first()
        if not product:
            return jsonify({"error": "Product not found or not available"}), 404

        # Create a new review
        new_review = ReviewModel(user_id=user_id, product_id=product_id, rating=rating, review=review)
        db.session.add(new_review)

        item_transcations = OrderItemModel.query.filter_by(product_id=product_id).first()

        if not item_transcations:
            return jsonify({"error": "No transactions found for the user"}), 404
        
        item_transcations.is_reviewed = True

        db.session.commit()
        return jsonify({"message": "Review added successfully", "data": new_review.to_dict()}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def edit_review(review_id, rating, review):
    try:
        # Check if the review exists
        review = ReviewModel.query.filter_by(id=review_id).first()
        if not review:
            return jsonify({"error": "Review not found"}), 404

        # Update the review
        review.rating = rating
        review.review = review
        db.session.commit()

        return jsonify({"message": "Review updated successfully", "data": review.to_dict()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def delete_review(review_id):
    try:
        # Check if the review exists
        review = ReviewModel.query.filter_by(id=review_id).first()
        if not review:
            return jsonify({"error": "Review not found"}), 404

        # Delete the review
        db.session.delete(review)
        db.session.commit()

        return jsonify({"message": "Review deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def get_all_reviews():
    try:
        # Fetch all reviews from the database
        reviews = ReviewModel.query.all()

        # Check if reviews exist
        if not reviews:
            return jsonify({"message": "No reviews found"}), 404

        # Return the review data in JSON format
        return jsonify({
            "data": [review.to_dict() for review in reviews]
        }), 200
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({
            "error": "An error occurred while fetching reviews.",
            "details": str(e)
        }), 500
    
def get_reviews_by_product_id(product_id):
    try:
        # Fetch reviews for a specific product from the database
        reviews = ReviewModel.query.filter_by(product_id=product_id).all()

        # Check if reviews exist
        if not reviews:
            return jsonify({"message": "No reviews found for the product"}), 404

        # Return the review data in JSON format
        return jsonify({
            "data": [review.to_dict() for review in reviews]
        }), 200
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({
            "error": "An error occurred while fetching reviews.",
            "details": str(e)
        }), 500
    