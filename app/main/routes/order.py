from flask import Blueprint
from flask import request
import json
from app.main.services.login_service import decode_auth_token
from app.main.services.order_services import *

order = Blueprint('order', __name__)

@order.route('/my_orders', methods=['GET'])
def my_orders():
    try:
        auth_token = request.headers.get("auth_token")
    except KeyError:
        return json.dumps({"status": False, "message": "No auth token"})

    data = decode_auth_token(auth_token)

    result = get_my_orders_db(data["user_id"])
    return json.dumps({"status": True, "My orders": result})

@order.route('/place_order', methods=['POST'])
def place_order():
    try:
        auth_token = request.headers.get("auth_token")
    except KeyError:
        return json.dumps({"status": False, "message": "No auth token"})
    
    data = decode_auth_token(auth_token)

    try:
        product_id = request.json["product_id"]
    except KeyError:
        return json.dumps({"status": False, "message": "select product"})
    result = place_order_db(data["user_id"],product_id)
    return json.dumps({"status": True, "message": "Order placed"})