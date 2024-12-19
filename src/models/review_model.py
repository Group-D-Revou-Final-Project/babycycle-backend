from datetime import datetime, timezone
from src.config.settings import db

class ReviewModel(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id', ondelete="CASCADE"), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    user = db.relationship('UserModel', back_populates='reviews')
    product = db.relationship('ProductModel', back_populates='reviews')

    def __repr__(self):
        return f'<ReviewModel id={self.id} user_id={self.user_id} product_id={self.product_id} rating={self.rating} review={self.review} created_at={self.created_at} updated_at={self.updated_at}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'product_id': self.product_id,
            'rating': self.rating,
            'review': self.review,
        }