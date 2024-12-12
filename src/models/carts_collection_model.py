from datetime import datetime, timezone
from src.config.settings import db

class CartsCollectionModel(db.Model):
    __tablename__ = 'carts_collection'

    id = db.Column(db.Integer, primary_key=True)
    carts_id = db.Column(db.Integer, db.ForeignKey('carts.id', ondelete="CASCADE"), nullable=False)  # Product reference
    
    
    # Relationship with ProductModel
    carts = db.relationship('CartModel', back_populates='cartscollection')
    
   
    def __repr__(self):
       return f"<CartsCollection(id={self.id}, carts_id={self.carts_id})>"

    
    def to_dict(self):
        return {
            "id": self.id,
            "carts_id": self.carts_id
        }