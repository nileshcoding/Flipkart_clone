from sqlalchemy import text
from app.main.settings import db
import json
from flask import request
from app.main.models.CategoriesModel import *

def search_product_db(filter):
    page = request.args.get('page', default=1, type=int)
    sql = text('SELECT id FROM category WHERE category_name=:filter;')
    
    try:
        category_id = db.engine.execute(sql, {"filter": filter}).fetchone().id
    except:
        category_id = None
        pass

    if category_id is None:
        sql = text('''SELECT * FROM product LIMIT :limit, 5;''')
        result =db.engine.execute(sql,{"limit": (page-1)*5})
        li_result = []

        for row in result:
            li_result.append({"product_id": row.id, "product_name": row.product_name, "product_price": row.product_price, "product_category_id": row.product_category_id})
        return li_result

    else:
        sql1 = text('SELECT product.*, category.category_name FROM product JOIN category on category.id=product.product_category_id JOIN treepath on treepath.descendants=category.id WHERE treepath.ancestor=:category_id LIMIT :limit,5;')
        result = db.engine.execute(sql1,{'category_id': category_id, "limit": (page-1)*5})
        li_result = []

        for row in result:
            li_result.append({"product_id": row.id, "product_name": row.product_name, "product_price": row.product_price, "product_category_id": row.product_category_id, "category_name": row.category_name})
        return li_result