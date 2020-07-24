from flask import Blueprint
from flask import request
import json

comments = Blueprint('comments', __name__)

@comments.route('/', methods=['GET'])
def get_comments():
    try:
        auth_token = request.headers.get("auth_token")
    except KeyError:
        return json.dumps({"status": False, "message": "No auth token"})

    try:
        product_id = request.json["product_id"]
    except KeyError:
        return json.dumps({"status": False, "message": "select product"})

    result = get_comments_db(product_id)
    return json.dumps({"status": True, "comments" : result})