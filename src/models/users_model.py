from datetime import datetime, timezone
from src.config.settings import db

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum('USER', 'ADMIN', name='role_type_enum'), default='USER', nullable=False)
    address = db.Column(db.Text, nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    is_seller = db.Column(db.Boolean, nullable=False, default=False)
    is_verified = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    verification = db.relationship('VerificationModel', back_populates='user', uselist=False, cascade="all, delete-orphan")
    # Define relationship to ProductModel
    # products = db.relationship('ProductModel', back_populates='user', cascade="all, delete-orphan")  # One-to-many relation with Product
    carts = db.relationship('CartModel', back_populates='user', cascade="all, delete-orphan")

    def __repr__(self):
        return f'<User {self.email}>'