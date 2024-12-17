from datetime import datetime, timezone
from src.config.settings import db

class CartsCollectionModel(db.Model):
    __tablename__ = 'carts_collection'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    carts_id = db.Column(db.Integer, db.ForeignKey('carts.id', ondelete="CASCADE"), nullable=False)  # Product reference
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    
    # Relationship with CartModel
    carts = db.relationship('CartModel', back_populates='cartscollection')
    
   
    def __repr__(self):
       return f"<CartsCollection(id={self.id}, carts_id={self.carts_id})>"

    
    def to_dict(self):
        return {
            "id": self.id,
            "carts_id": self.carts_id
        }