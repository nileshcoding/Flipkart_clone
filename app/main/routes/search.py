from flask import Blueprint
from flask import request
import json
from app.main.services.login_service import decode_auth_token
from app.main.services.search_services import *
search = Blueprint('search', __name__)

@search.route('/', methods=['GET'])
def search_product():
    try:
        auth_token = request.headers.get("auth_token")
    except KeyError:
        return json.dumps({"status": False, "message": "No auth token"})

    category_id = None

    try:
        filter = request.args.get('filter',default=None)
    except KeyError:
        pass
    except TypeError:
        pass

    result = search_product_db(filter)
    return json.dumps({"status": True, "products": result})