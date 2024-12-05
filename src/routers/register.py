from flask import Blueprint, request
from src.config.settings import db
from src.services.user_service import (
    create_user_account,
    verify_user_account,
    resend_verification_code,
    forgot_password,
    reset_password
)

register_blueprint = Blueprint('users', __name__)

@register_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    return create_user_account(username=username, email=email, password=password)
    

@register_blueprint.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    email = data.get('email')
    verification_code = data.get('verification_code')

    return verify_user_account(email=email, verification_code=verification_code)

@register_blueprint.route('/resend_verification', methods=['POST'])
def resend_verification():
    data = request.get_json()
    email = data.get('email')

    # Call the resend_verification_code function
    return resend_verification_code(email)

@register_blueprint.route('/forgot-password', methods=['POST'])
def forgot_password_route():
    data = request.get_json()
    email = data.get('email')

    # Call the send_forgot_password_email function
    return forgot_password(email)

@register_blueprint.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password_route(token):
    data = request.get_json()
    new_password = data.get('new_password')

    return reset_password(token, new_password)