from flask import Blueprint
from flask import request
from app.main.services.login_service import decode_auth_token
from app.main.services.product_services import *

products = Blueprint('products', __name__)

@products.route('/', methods=['GET'])
def get_products():
    page = request.args.get('page', default=1, type=int)
    data = all_products(page)
    return json.dumps({"products": data})


@products.route('/add', methods=['POST'])
def add_product():
    try:
        auth_token = request.headers.get("auth_token")
    except KeyError:
        return json.dumps({"status": False, "message": "Log in to add product"})

    data = decode_auth_token(auth_token)
    if data["role"] == "owner":
        try:
            product_name = request.json["product_name"]
            product_price = request.json["product_price"]
            product_category_id = request.json["product_category_id"]
        except KeyError:
            return json.dumps({"status": False, "message": "Enter all fields"})

        data = add_product_db(product_name,product_price,product_category_id)
        return data
    else:
        return json.dumps({"status": False, "message": "user not allowed to add product"})

@products.route('/update', methods=['POST'])
def update_product():
    try:
        auth_token = request.headers.get("auth_token")
    except KeyError:
        return json.dumps({"status": False, "message": "provide auth token"})

    data = decode_auth_token(auth_token)

    if data["role"] == "owner" or data["role"] == "admin":
        try:
            product_id = request.json["product_id"]
            product_name = request.json["product_name"]
            product_price = request.json["product_price"]
            product_category_id = request.json["product_category_id"]
        except KeyError:
            return json.dumps({"status": False, "message": "Enter all fields"})
        
        result = update_product_db(product_id,product_name,product_price,product_category_id)
        return result
    else:
        return json.dumps({"status": False, "message": "User not aloowed to modify product"})


@products.route('/delete', methods=['POST'])
def delete_product():
    try:
        auth_token = request.headers.get("auth_token")
    except KeyError:
        return json.dumps({"status": False, "message": "No auth token"})

    data = decode_auth_token(auth_token)

    if data["role"] == "owner" or data["role"] == "admin":
        try:
            product_id = request.json["product_id"]
        except KeyError:
            return json.dumps({"status": False, "message": "Enter all fields"})

        result = delete_product_db(product_id)
        return result
    else:
        return json.dumps({"status": True, "message": "User not allowed to delete product"})

