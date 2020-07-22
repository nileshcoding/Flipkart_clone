from flask import Blueprint
from flask import request
from app.main.services.login_service import *
from app.main.models.UserModel import User
import time
import json

login = Blueprint('login', __name__)

@login.route('/', methods=['POST'])
def user_login():
    try:
        email = request.json["email"]
        password = request.json["password"]
    except KeyError:
        return json.dumps({"status": False, "message": "Usernam or Password not entered"})

    user =  User.query.filter_by(email=email).first()
    if user == None:
        return json.dumps({"status": False, "message": "User does not exist"})
    
    payload = {"user_id": user.id, "email": user.email, "role": user.role, "address": user.address, "expire": time.time()+3600}

    if user.password == password:
        encoded_payload = encode_jwt(payload)
        return json.dumps({"status": True, "auth_token": encoded_payload.decode(), "message": "user logged in"})
    else:
        return json.dumps({"status": False, "message": "email or password incorrect"})