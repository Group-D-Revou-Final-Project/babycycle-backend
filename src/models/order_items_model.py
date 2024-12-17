from datetime import datetime, timezone
from src.config.settings import db
from src.models.orders_model import OrderModel
from src.models.products_model import ProductModel


class OrderItemModel(db.Model):
    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id', ondelete="CASCADE"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    

    order = db.relationship('OrderModel', back_populates='order_items')
    product = db.relationship('ProductModel', back_populates='order_items')

    def __repr__(self):
        return f'<OrderItem {self.product.name}, Quantity: {self.quantity}>'