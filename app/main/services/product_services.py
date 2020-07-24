from app.main.settings import db
from app.main.models.ProductModel import *
import json
from sqlalchemy import text

def all_products(page):
    per_page = 2
    sql = text('SELECT * FROM  product LIMIT :limit,5')
    result = db.engine.execute(sql,{"limit": (page-1)*5})
    li_products = []
    for row in result:
        li_products.append({"product_id": row.id, "product_name": row.product_name, "product_price": row.product_price, "product_category_id": row.product_category_id})
    return li_products



def add_product_db(productname,productprice,productcategory_id):
    product = Product(product_name=productname,product_price=productprice, product_category_id=productcategory_id)
    try:
        db.session.add(product)
        db.session.commit()
        return json.dumps({"status": True, "message": "Product added"})
    except:
        return  json.dumps({"status": False, "message": "try again"})


def update_product_db(product_id,productname,product_price,productcategory_id):
    product = Product.query.get(product_id)
    product.product_name = productname
    product.product_price = product_price
    product.product_category_id = productcategory_id

    try:
        db.session.commit()
        return json.dumps({"status": True, "message": "product updated"})
    except:
        return json.dumps({"status": False, "message": "Try again"})


def delete_product_db(product_id):
    product = Product.query.get(product_id)
    
    try:
        db.session.delete(product)
        db.session.commit()
        return json.dumps({"status": True, "message": "Product deleted"})
    except:
        return json.dumps({"status": False, "message": "Try again"})
