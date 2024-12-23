from datetime import datetime, timezone
from src.config.settings import db

class ProductModel(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)  # Primary key
    seller_id = db.Column(db.Integer, db.ForeignKey('sellers.id', ondelete="CASCADE"), nullable=True)
    name = db.Column(db.String(255), nullable=False)  # Product name
    price = db.Column(db.Float, nullable=False)  # Product price
    descriptions = db.Column(db.Text, nullable=True)  # Optional description
    category = db.Column(db.String(255), nullable=False)  # Product category
    is_warranty = db.Column(db.Boolean, nullable=False, default=False)  # Boolean for warranty
    image_url = db.Column(db.String(255), nullable=True)  # URL of the product image
    stock = db.Column(db.Integer, nullable=False, default=0)  # Product stock
    is_deactivated = db.Column(db.Boolean, nullable=False, default=False)
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))  # Creation time
    updated_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))  # Update time


    # Use string references to avoid circular import issues
    discounts = db.relationship('DiscountModel', back_populates='product', cascade="all, delete-orphan")
    carts = db.relationship('CartModel', back_populates='product', cascade="all, delete-orphan")
    seller = db.relationship('SellerModel', back_populates='products')
    order_items = db.relationship('OrderItemModel', back_populates='product')
    reviews = db.relationship('ReviewModel', back_populates='product', cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Product(name={self.name}, price={self.price}, category={self.category}), stock={self.stock}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'descriptions': self.descriptions,
            'category': self.category,
            'is_warranty': self.is_warranty,
            'image_url': self.image_url,
            'stock': self.stock,
            # 'user_id': self.user_id,
            'created_at': self.created_at
        }