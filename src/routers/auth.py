from flask import Blueprint, request
from flasgger import swag_from
from src.services.user_service import (
    login_user
)
from src.swagger.users_swagger import (
    LOGIN_USER,
)

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
@swag_from(LOGIN_USER)
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    return login_user(email=email, password=password)