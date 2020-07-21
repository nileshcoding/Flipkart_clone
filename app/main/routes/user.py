from flask import Blueprint
from flask import request
import json
import jwt
from app.main.services.user_services import *
from app.main.services.login_service import *

user = Blueprint('user', __name__)

@user.route('/register', methods=['POST'])
def register_user():
    try:
        name = request.json["name"]
        email = request.json["email"]
        password = request.json["password"]
        role = request.json["role"]
    except KeyError:
        return json.dumps({"status": True, "message": "Enter all fields"})

    add_user(name,email,password,role)
    return json.dumps({"status": True, "message": "User registered"})


@user.route('/delete', methods=['POST'])
def delete_user():
    try:
        auth_token = request.headers.get("auth_token")
    except KeyError:
        return json.dumps({"status": False, "message": "Give auth token"})

    data = decode_auth_token(auth_token)
    if data["role"] == "admin":
        try:
            user_id = request.json["user_id"]
        except KeyError:
            return json.dumps({"status": False, "message": "Enter user id"})