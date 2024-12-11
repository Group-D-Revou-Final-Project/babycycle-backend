from flask import jsonify, current_app, url_for
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from datetime import datetime, timezone
from src.services.validator import Validator
from src.models.users_model import UserModel
from src.models.verifications_model import VerificationModel
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
# import random
# import string
import os
from dotenv import load_dotenv

from src.config.settings import db

load_dotenv()

# s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
def create_user_account(username, email, password):

    # Validate email
    validation_response, status_code = Validator.email_validation(email_request=email)
    if status_code != 200:
        # normalized_email = validation_response
        return validation_response, status_code
    
    # normalized_email = validation_response['email']

   # Check if the user already exists
    user_email = UserModel.query.filter_by(email=email).first()
    user_name = UserModel.query.filter_by(username=username).first()
    if user_email or user_name:
        return jsonify({"error": "Account is already registered."}), 400
    
    # Create a new user
    hashed_password = generate_password_hash(password)
    new_user = UserModel(email=email, username=username, password_hash=hashed_password)


    # Create a new verification record and associate it with the user
    new_verification = VerificationModel()
    new_verification.generate_verification_code()

    # Associate the new verification record with the user
    new_user.verification = new_verification

    # Add the user and verification records to the database
    db.session.add(new_user)
    db.session.add(new_verification)
    db.session.commit()

    # Send the verification code to the user's email
    return Validator.send_verification_email(email, new_verification.verification_code)

    # return jsonify({"message": "Registration successful! Please check your email for the verification code."}), 200

def resend_verification_code(email):
    # Check if the user exists
    user = UserModel.query.filter_by(email=email).first()

    if not user:
        return jsonify({"error": "User not found."}), 404
    
    # Check if the user is already verified
    if user.is_verified:
        return jsonify({"message": "User is already verified."}), 400

    # Get the user's verification record
    verification = user.verification

    # Check if the verification record exists
    if not verification:
        return jsonify({"error": "Verification record not found."}), 404

    # Ensure that the code expiration time is aware (in UTC)
    if verification.code_expiration.tzinfo is None:
        verification.code_expiration = verification.code_expiration.replace(tzinfo=timezone.utc)

    # Check if the code has expired
    if datetime.now(timezone.utc) > verification.code_expiration:
        # If the code expired, regenerate the verification code and expiration
        verification.generate_verification_code()

        # Update the database with the new verification code and expiration time
        db.session.commit()

    # Send the verification email with the (possibly new) verification code
    return Validator.send_verification_email(email, verification.verification_code)

    # return jsonify({"message": "Verification code resent successfully! Please check your email."}), 200


def verify_user_account(email, verification_code):
    # Check if the user exists
    user = UserModel.query.filter_by(email=email).first()

    if not user:
        return jsonify({"error": "User not found."}), 404

    # Get the user's verification code and expiration time
    verification = user.verification

    # Ensure that the expiration time is aware (in UTC)
    if verification.code_expiration.tzinfo is None:
        verification.code_expiration = verification.code_expiration.replace(tzinfo=timezone.utc)

    # Check if the code has expired
    if datetime.now(timezone.utc) > verification.code_expiration:
        return jsonify({"error": "Verification code has expired."}), 400

    # Check if the code matches
    if verification.verification_code != verification_code:
        print(verification.verification_code)
        print(f'verification_code input ${verification_code}')
        return jsonify({"error": "Invalid verification code."}), 400

    # Mark the user as verified
    user.is_verified = True
    db.session.commit()

    return jsonify({"message": "Email verified successfully!"}), 200

### FORGOT PASSWORD
def forgot_password(email):
    s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])

    user = UserModel.query.filter_by(email=email).first()

    if not email:
        return jsonify({"error": "Email is required."}), 400

    if user:
        # Generate a reset token
        token = s.dumps(email, salt=os.getenv('RESET_PASSWORD_SALT'))

        # Create the reset URL (the link the user will click)
        reset_url = url_for('users.reset_password_route', token=token, _external=True, _scheme='https')

        verification = user.verification

        if verification is not None:
            verification.url_reset_password = reset_url
            db.session.commit()
        
        


        try:
            return Validator.send_forgot_password_email(user_email=email, url_link=reset_url)
        except Exception as e:
            return jsonify({"error": f"Error sending email: {str(e)}"}), 500
    else:
        return jsonify({"error": "This email is not registered."}), 404
    
def reset_password(token, new_password):

    s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])

    if not token:
        return jsonify({"error": "Token is required."}), 400
    
    if not new_password:
        return jsonify({"error": "New password is required."}), 400

    try:
        # Verify the token and get the email
        email = s.loads(token, salt=os.getenv('RESET_PASSWORD_SALT'), max_age=3600)  # Token expires in 1 hour

        # Hash the new password and update in the "database"
        hashed_password = generate_password_hash(new_password)
        user = UserModel.query.filter_by(email=email).first()
        user.password_hash = hashed_password
        db.session.commit()

        return jsonify({"message": "Your password has been updated."}), 200

    except SignatureExpired:
        return jsonify({"error": "The reset link has expired."}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    
def login_user(email, password):
    
    user = UserModel.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "Invalid email or password"}), 404

    
    if not check_password_hash(user.password_hash, password):
        return jsonify({"error": "Invalid email or password"}), 401

    
    if not user.is_verified:
        return jsonify({"error": "Email is not verified. Please verify your email first."}), 403

    additional_claims = {
        'id': user.id,
        'role': user.role,  
        'is_seller': user.is_seller  
    }

    
    access_token = create_access_token(identity=str(user.id), additional_claims=additional_claims)

    return jsonify({
        "message": "Login successful",
        "access_token": access_token
    }), 200

