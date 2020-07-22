from app.main.settings import db
from app.main.models.ProductModel import *
import json

def all_products():
    products = Product.query.all()
    li_products = []
    for row in products:
        li_products.append([row.product_name, row.product_price])
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
        return json.dumps({"status": True, "productname": product.product_name,"message": "product updated"})
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
