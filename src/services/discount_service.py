from flask import jsonify

from src.models.products_model import ProductModel
from src.models.discounts_model import DiscountModel

def get_discount_by_id(product_id):
    discount = DiscountModel.query.filter_by(product_id=product_id, is_active=True).first()
    if discount:
        return jsonify(discount.to_dict()), 200
    else:
        return jsonify({"error": "Discount not found"}), 404

def get_calculated_discount(product_id):
    try:
        discount = DiscountModel.query.filter_by(product_id=product_id, is_active=True).first()
        if discount:

            product = ProductModel.query.filter_by(id=product_id, is_deleted=False).first()
            if product:
                discounted_price = discount.get_discounted_price(product.price)
                return jsonify({"discounted_price": discounted_price}), 200
            else:
                return jsonify({"error": "Discount Product not found"}), 404
            # return jsonify(discount.to_dict()), 200
        else:
            return jsonify({"error": "Discount not found"}), 404
        

    except Exception as e:
        return jsonify({"error": str(e)}), 500
