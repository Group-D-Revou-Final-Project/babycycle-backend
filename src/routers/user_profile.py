from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.services.user_service import (
    update_user_image,
    update_user_profile
)

user_profile_bp = Blueprint('user_profile', __name__)


@user_profile_bp.route('/users/profile/image', methods=['PUT'])
# @swag_from(GET_USER_PROFILE)
@jwt_required()
def update_user_image_route():
    data = request.get_json()
    userID = get_jwt_identity()
    profile_image = data.get('profile_image')
    return update_user_image(user_id=userID, profile_image=profile_image)

@user_profile_bp.route('/users/profile', methods=['PUT'])
# @swag_from(GET_USER_PROFILE)
@jwt_required()
def update_user_profile_route():
    data = request.get_json()
    userID = get_jwt_identity()
    username = data.get('username')
    email = data.get('email')
    phone = data.get('phone')
    return update_user_profile(user_id=userID, username=username, email=email, phone=phone)