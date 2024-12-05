from datetime import datetime, timezone, timedelta
from src.config.settings import db

class VerificationModel(db.Model):
    __tablename__ = 'verifications'
    id = db.Column(db.Integer, primary_key=True)
    verification_code = db.Column(db.String(6), nullable=False)
    code_expiration = db.Column(db.DateTime, nullable=False)
    url_reset_password = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))


    # Foreign key relationship with the User table
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)

    # Define the back reference to the User model
    user = db.relationship('UserModel', back_populates='verification')

    def generate_verification_code(self):
        """Generate a random 6-digit verification code."""
        import random
        self.verification_code = str(random.randint(100000, 999999))
        self.code_expiration = datetime.now(timezone.utc) + timedelta(minutes=15)