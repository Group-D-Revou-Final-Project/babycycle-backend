from flask import Blueprint, request
from flasgger import swag_from
from src.services.user_service import (
    create_user_account,
    verify_user_account,
    resend_verification_code,
    forgot_password,
    reset_password,
    get_user_by_id,
    get_all_users
    )
from src.swagger.users_swagger import (
    REGISTER_USER,
    VERIFY_USER,
    RESEND_VERIFICATION,
    FORGOT_PASSWORD,
    RESET_PASSWORD,
    GET_ALL_USERS,
    GET_USER_BY_ID
)

from flask_jwt_extended import jwt_required

register_blueprint = Blueprint('users', __name__)

@register_blueprint.route('/register', methods=['POST'])
@swag_from(REGISTER_USER)
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    return create_user_account(username=username, email=email, password=password)
    

@register_blueprint.route('/verify', methods=['POST'])
@swag_from(VERIFY_USER)
def verify():
    data = request.get_json()
    email = data.get('email')
    verification_code = data.get('verification_code')

    return verify_user_account(email=email, verification_code=verification_code)

@register_blueprint.route('/resend_verification', methods=['POST'])
@swag_from(RESEND_VERIFICATION)
def resend_verification():
    data = request.get_json()
    email = data.get('email')

    # Call the resend_verification_code function
    return resend_verification_code(email)
@register_blueprint.route('/forgot-password', methods=['POST'])
@jwt_required()
@swag_from(FORGOT_PASSWORD)
def forgot_password_route():
    data = request.get_json()
    email = data.get('email')

    # Call the send_forgot_password_email function
    return forgot_password(email)

@register_blueprint.route('/reset-password/<token>', methods=['POST'])
@swag_from(RESET_PASSWORD)
def reset_password_route(token):
    data = request.get_json()
    new_password = data.get('new_password')

    return reset_password(token, new_password)

@register_blueprint.route('/<user_id>', methods=['GET'])
@swag_from(GET_USER_BY_ID)
def get_user_from_id_route(user_id):
    # Call the get_user_from_id function
    return get_user_by_id(user_id)

@register_blueprint.route('/', methods=['GET'])
@swag_from(GET_ALL_USERS)
def get_all_users_route():
    # Call the get_all_users function
    return get_all_users()