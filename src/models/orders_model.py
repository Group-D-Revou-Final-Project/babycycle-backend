from datetime import datetime, timezone
from src.config.settings import db
# from src.models.users_model import UserModel
# from src.models.sellers_model import SellerModel
# from src.models.order_items_model import OrderItemModel


class OrderModel(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('sellers.id'), nullable=True)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='pending')
    payment_method = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    user = db.relationship('UserModel', back_populates='orders')
    seller = db.relationship('SellerModel', back_populates='order') 
    order_items = db.relationship('OrderItemModel', back_populates='order')

    def __repr__(self):
        return f'<Order {self.id}>'