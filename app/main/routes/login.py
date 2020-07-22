from flask import Blueprint
from flask import request
from app.main.services.login_service import *
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

    user =  User.query.filter_by(email=email)

    if user == None:
        return json.dumps({"status": True, "message": "User does not exist"})
    
    paylaod = {"user_id": user.id, "email": user.email, "role": user.role, "expire": time.time()+3600}

    if user.password == password:
        encoded_payload = encode_jwt(payload)
        return json.dumps({"status": True, "auth_token": encoded_payload.decode(), "message": "user logged in"})
    else:
        return json.dumps({"status": True, "message": "email or password incorrect"})