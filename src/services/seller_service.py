from flask import jsonify
from src.models.users_model import UserModel
from src.models.sellers_model import SellerModel
from src.models.products_model import ProductModel
from src.models.review_model import ReviewModel
from src.models.discounts_model import DiscountModel
from src.config.settings import db


def get_sellers():
    sellers = SellerModel.query.all()
    return [seller.to_dict() for seller in sellers]

def get_seller_by_id(seller_id):
    seller = SellerModel.query.get(seller_id)
    return seller.to_dict()

# def get_seller_by_user_id(user_id):
#     seller = SellerModel.query.filter_by(user_id=user_id).first()
#     return seller

def create_seller(user_id, name, address, contact):
    try:
        user = UserModel.query.get(user_id)
        if user is None:
            return jsonify({"error": "User not found"}), 404

        new_seller = SellerModel(user_id=user_id, name=name, address=address, contact=contact)
        db.session.add(new_seller)
        db.session.commit()

        return jsonify({"message": "Seller created successfully", "data": new_seller.to_dict()}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def update_seller(seller_id, name, address, contact):
    try:
        seller = SellerModel.query.get(seller_id)
        if seller is None:
            return jsonify({"error": "Seller not found"}), 404

        seller.name = name
        seller.address = address
        seller.contact = contact
        db.session.commit()

        return jsonify({"message": "Seller updated successfully", "data": seller.to_dict()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def delete_seller(seller_id):
    try:
        seller = SellerModel.query.get(seller_id)
        if seller is None:
            return jsonify({"error": "Seller not found"}), 404

        db.session.delete(seller)
        db.session.commit()

        return jsonify({"message": "Seller deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_products_by_seller(user_id):

    seller = SellerModel.query.filter_by(user_id=user_id).first()
    if seller is None:
        return jsonify({"error": "Seller not found"}), 404

    seller_id = seller.id


    results = db.session.query(
        ProductModel.name.label("name"),
        ReviewModel.rating.label("rating"),
        ProductModel.price.label("price"),
        DiscountModel.discount_percentage.label("discount_percentage"),
        ProductModel.stock.label("stock"),
        ProductModel.seller_id.label("seller_id")
    ).outerjoin(
        ReviewModel, ReviewModel.product_id == ProductModel.id
    ).outerjoin(
        DiscountModel, DiscountModel.product_id == ProductModel.id
    ).filter(
        ProductModel.seller_id == seller_id
    ).all()
    if not results:
        return jsonify({"error": "No products found for the specified seller"}), 404

    # Format the results as a list of dictionaries
    formatted_results = [
        {
            "name": result.name,
            "rating": result.rating,
            "price": result.price,
            "discount_percentage": result.discount_percentage,
            "stock": result.stock,
            "seller_id": result.seller_id
        }
        for result in results
    ]

    return jsonify(formatted_results), 200