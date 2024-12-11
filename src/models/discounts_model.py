from datetime import datetime, timezone
from decimal import Decimal
from src.config.settings import db

class DiscountModel(db.Model):
    __tablename__ = 'discounts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id', ondelete="CASCADE"), nullable=False)  # Relation to Product
    discount_percentage = db.Column(db.Numeric(5, 2), nullable=False)  # Discount percentage
    discount_amount = db.Column(db.Numeric(10, 2), nullable=True)  # Optional: Fixed discount amount
    start_date = db.Column(db.DateTime, nullable=True)  # Optional: Discount start date
    end_date = db.Column(db.DateTime, nullable=True)  # Optional: Discount end date
    is_active = db.Column(db.Boolean, default=True)  # Whether the discount is active or not

    product = db.relationship('ProductModel', back_populates='discounts')  # Backref for reverse relation

    def __repr__(self):
        return f"<Discount(product_id={self.product_id}, discount_percentage={self.discount_percentage}, active={self.active})>"


    def get_discounted_price(self, product_price):
        """Calculate discounted price."""
        if self.discount_percentage:
            # Ensure both operands are of type Decimal
            product_price = Decimal(str(product_price))  # Convert float to Decimal
            return product_price * (1 - self.discount_percentage / Decimal('100'))  # Use Decimal for arithmetic
        elif self.discount_amount:
            return product_price - self.discount_amount
        return product_price
    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "discount_percentage": self.discount_percentage,
            "discount_amount": self.discount_amount,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "is_active": self.is_active
        }