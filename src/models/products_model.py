from datetime import datetime, timezone, timedelta
from src.config.settings import db

class ProductModel(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)  # Primary key
    name = db.Column(db.String(255), nullable=False)  # Product name
    price = db.Column(db.Float, nullable=False)  # Product price
    description = db.Column(db.Text, nullable=True)  # Optional description
    category = db.Column(db.String(255), nullable=False)  # Product category
    is_warranty = db.Column(db.Boolean, nullable=False, default=False)  # Boolean for warranty
    image_url = db.Column(db.String(255), nullable=True)  # URL of the product image
    stock = db.Column(db.Integer, nullable=False, default=0)  # Product stock
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))  # Creation time
    updated_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))  # Update time

    # Foreign key and relationship with UserModel
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    user = db.relationship('UserModel', back_populates='products')  # Relationship back to UserModel

    def __repr__(self):
        return f'<Product(name={self.name}, price={self.price}, category={self.category})>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'category': self.category,
            'is_warranty': self.is_warranty,
            'image_url': self.image_url,
            'stock': self.stock
        }