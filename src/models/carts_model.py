from datetime import datetime, timezone
from src.config.settings import db

class CartModel(db.Model):
    __tablename__ = 'carts'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id', ondelete="CASCADE"), nullable=False)  # Product reference
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)  # User reference
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    user_address = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))  # Creation time
    updated_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))  # Update time
    

    # Relationship with ProductModel
    product = db.relationship('ProductModel', back_populates='carts')
    
    # Relationship with UserModel
    user = db.relationship('UserModel', back_populates='carts')

    cartscollection = db.relationship('CartsCollectionModel', back_populates='carts')   

    def __repr__(self):
        return f"<Cart(user_id={self.user_id}, product_id={self.product_id}, quantity={self.quantity}, total_price={self.total_price})>"

    def calculate_total_price(self):
        """Calculate the total price for the cart item (quantity * price of the product)."""
        return self.quantity * self.product.price
    
    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            # "user_id": self.user_id,
            "quantity": self.quantity,
            "total_price": self.total_price,
            "user_address": self.user_address,
        }