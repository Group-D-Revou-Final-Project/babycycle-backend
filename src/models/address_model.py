from datetime import datetime, timezone
from src.config.settings import db

class AddressModel(db.Model):
    __tablename__ = 'addresses'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    contact = db.Column(db.String(50), nullable=False)
    address = db.Column(db.Text, nullable=False)
    is_main = db.Column(db.Boolean, nullable=True, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    user = db.relationship('UserModel', back_populates='addresses')
    
    # __table_args__ = (
    #     db.UniqueConstraint('user_id', 'is_main', name='unique_main_address_per_user'),
    # )
    def __repr__(self):
        return f"AddressModel(id={self.id}, user_id={self.user_id}, address={self.address}, created_at={self.created_at}, updated_at={self.updated_at})"
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'contact': self.contact,
            'address': self.address,
            'is_main': self.is_main,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }