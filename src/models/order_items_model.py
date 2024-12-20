from datetime import datetime, timezone
from src.config.settings import db
# from src.models.orders_model import OrderModel
# from src.models.products_model import ProductModel


class OrderItemModel(db.Model):
    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True)
    # order_id = db.Column(db.Integer, db.ForeignKey('orders.id', ondelete="CASCADE"), nullable=True)
    checkout_order_id = db.Column(
        db.String(255),
        db.ForeignKey('orders.checkout_id', ondelete="CASCADE"),
        nullable=False
    )
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    user_address = db.Column(db.Text, nullable=False)
    is_reviewed = db.Column(db.Boolean, nullable=True, default=False)

    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    

    order = db.relationship('OrderModel', back_populates='order_items')
    product = db.relationship('ProductModel', back_populates='order_items')

    def __repr__(self):
        return f'<OrderItem {self.product.name}, Quantity: {self.quantity}>'
    
    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "total_price": self.total_price,
            "user_address": self.user_address,
            "checkout_order_id": self.checkout_order_id,
            "is_reviewed": self.is_reviewed
        }