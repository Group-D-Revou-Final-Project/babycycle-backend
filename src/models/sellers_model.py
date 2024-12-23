from datetime import datetime, timezone
from src.config.settings import db
class SellerModel(db.Model):
    __tablename__ = 'sellers'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.Text, nullable=False)
    contact = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))


    user = db.relationship('UserModel', back_populates='seller')
    products = db.relationship('ProductModel', back_populates='seller', cascade="all, delete-orphan")
    order = db.relationship('OrderModel', back_populates='seller')


    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'address': self.address,
            'contact': self.contact,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }