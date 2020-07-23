from sqlalchemy import text
from app.main.settings import db
import json


def search_product_db(category_id):
    if category_id is None:
        sql = text('''SELECT product.product_name, product.product_price FROM product;''')
        result =db.engine.execute(sql)
        li_result = []
        for row in result:
            li_result.append(str(row))
        return li_result
    else:
        sql = text('SELECT product.product_name,product.product_price,category.category_name FROM product JOIN category on category.id=product.product_category_id JOIN treepath on treepath.descendants=category.id WHERE treepath.ancestor=:category_id;')
        result = db.engine.execute(sql,{'category_id': category_id})
        
        li_result = []
        for row in result:
            li_result.append(str(row))
        return li_result