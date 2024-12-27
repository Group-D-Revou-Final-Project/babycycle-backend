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
        ProductModel.id.label("id"),
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

    total_count = results.count()
    if not results:
        return jsonify({"error": "No products found for the specified seller"}), 404

    # Format the results as a list of dictionaries
    formatted_results = [
        {   
            "id": result.id,
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

def get_products_by_seller_v2(user_id):
    try:
        # Check if the seller exists
        seller = SellerModel.query.filter_by(user_id=user_id).first()
        if seller is None:
            return jsonify({"error": "Seller not found"}), 404

        seller_id = seller.id

        # Query to get product details, reviews, and discounts
        query = db.session.query(
            ProductModel.id.label("id"),
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
        )

        # Get total count
        total_count = query.count()

        # Fetch results
        results = query.all()

        # Return 404 if no products are found
        if not results:
            return jsonify({"error": "No products found for the specified seller"}), 404

        # Format the results
        formatted_results = {
            "total_count": total_count,
            "data": [
                {
                    "id": result.id,
                    "name": result.name,
                    "rating": result.rating or None,  # Handle null ratings
                    "price": float(result.price),
                    "discount_percentage": float(result.discount_percentage) if result.discount_percentage else 0.0,
                    "stock": result.stock,
                    "seller_id": result.seller_id,
                }
                for result in results
            ]
        }

        return jsonify(formatted_results), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def get_products_by_seller_v3(user_id):
    try:
        # Check if the seller exists
        seller = SellerModel.query.filter_by(user_id=user_id).first()
        if seller is None:
            return jsonify({"error": "Seller not found"}), 404

        seller_id = seller.id

        results = db.session.query(
            ProductModel.id,
            ProductModel.name,
            ProductModel.price,
            ProductModel.seller_id,
            ProductModel.image_url,
            ProductModel.is_warranty,
            ProductModel.stock,
            ProductModel.created_at,
            DiscountModel.discount_percentage,
            DiscountModel.start_date,
            DiscountModel.end_date,
            DiscountModel.is_active,
            ReviewModel.rating,
            ReviewModel.review
        ).outerjoin(
            DiscountModel, DiscountModel.product_id == ProductModel.id
        ).outerjoin(
            ReviewModel, ReviewModel.product_id == ProductModel.id
        ).filter(
            ProductModel.is_deactivated == False,
            ProductModel.is_deleted == False,
            ProductModel.seller_id == seller_id
        ).all()

        if not results:
            return jsonify({"error": "No products found for the specified seller"}), 404

        # Format the results as a list of dictionaries
        formatted_results = [
            {
                "id": result.id,
                "name": result.name,
                "price": float(result.price),
                "seller_id": result.seller_id,
                "image_url": result.image_url,
                "is_warranty": result.is_warranty,
                "stock": result.stock,
                "created_at": result.created_at.isoformat(),
                "discount_percentage": float(result.discount_percentage) if result.discount_percentage else 0.0,
                "start_date": result.start_date.isoformat() if result.start_date else None,
                "end_date": result.end_date.isoformat() if result.end_date else None,
                "is_active": result.is_active,
                "rating": result.rating,
                "review": result.review
            }
            for result in results
        ]

        return jsonify(formatted_results), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
def get_seller_by_product_id(product_id):
    try:
        result = db.session.query(
            SellerModel.id,
            SellerModel.user_id,
            SellerModel.name,
            SellerModel.address,
            SellerModel.contact,
            SellerModel.created_at,
            SellerModel.updated_at
        ).outerjoin(
            ProductModel, ProductModel.seller_id == SellerModel.id
        ).filter(
            ProductModel.id == product_id
        ).first()

        if not result:
            return jsonify({"error": "Seller not found for the specified product"}), 404

        # Format the result as a dictionary
        seller_data = {
            "seller_id": result.id,
            "user_id": result.user_id,
            "name": result.name,
            "address": result.address,
            "contact": result.contact,
            "created_at": result.created_at.isoformat(),
            "updated_at": result.updated_at.isoformat() if result.updated_at else None
        }

        return jsonify(seller_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500