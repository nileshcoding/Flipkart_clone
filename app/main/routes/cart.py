from flask import Blueprint
from flask import request
import json
import jwt
from app.main.services.login_service import decode_auth_token
from app.main.services.cart_services import *

cart = Blueprint('cart', __name__)

@cart.route('/my_cart', methods=['GET'])
def my_cart():
    try:
        auth_token = request.headers.get("auth_token")
    except KeyError:
        return json.dumps({"status": False, "message": "No auth token"})

    data = decode_auth_token(auth_token)

    result = get_my_cart(data["user_id"])
    return json.dumps({"status": True, "cart": str(result)})


@cart.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    try:
        auth_token = request.headers.get("auth_token")
    except KeyError:
        return json.dumps({"status": False, "message": "No auth token"})

    try:
        product_id = request.json["product_id"]
    except KeyError:
        return json.dumps({"status": False, "message": "No product selected"})

    data = decode_auth_token(auth_token)

    result = add_to_cart_db(data["user_id"],product_id)
    return json.dumps({"status": True, "message": "Product added to cart"})