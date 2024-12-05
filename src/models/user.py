# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash
# # from email_validator import validate_email, EmailNotValidError
# from flask_login import UserMixin

# db = SQLAlchemy()

# class User(db.Model, UserMixin):
#     __tablename__ = 'users'

#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(255), unique=True, nullable=False)
#     email = db.Column(db.String(255), unique=True, nullable=False)
#     password_hash = db.Column(db.String(255), nullable=False)
#     address = db.Column(db.Text, nullable=True)
#     phone = db.Column(db.String(255), nullable=True)
#     is_seller = db.Column(db.Boolean, default=False)
#     is_verified = db.Column(db.Boolean, default=False)

#     def __init__(self, username, email, password, address=None, phone=None, is_seller=False, is_verified=False):
#         """Initialize a new user instance."""
        
#         # Validasi email sebelum menyimpannya
#         self.validate_email(email)

#         self.username = username
#         self.email = email
#         self.password_hash = generate_password_hash(password)
#         self.address = address
#         self.phone = phone
#         self.is_seller = is_seller
#         self.is_verified = is_verified

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)

#     def __repr__(self):
#         return f'<User {self.username}>'
