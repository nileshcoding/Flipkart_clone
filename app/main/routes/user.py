from flask import Blueprint
from flask import request
import json
import jwt
from app.main.services.user_services import *

user = Blueprint('user', __name__)

@user.route('/register', methods=['POST'])
def register_user():
    try:
        name = request.json["name"]
        email = request.json["email"]
        password = request.json["password"]
        role = request.json["role"]
    except KeyError:
        return json.dumpd({"status": True, "message": "Enter all fields"})

    add_user(name,email,password,role)
    return json.dumps({"status": True, "message": "User registered"})
