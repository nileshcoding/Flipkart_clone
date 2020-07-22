from app.main.settings import db
from app.main.models.ProductModel import *
import json

def all_products():
    return Product.query.all()


def add_product_db(productname,productcategory_id):
    product = Product(productname=prodauctname, productcategory_id=productcategory_id)
    try:
        db.session.add(product)
        db.session.commit()
        return json.dumps({"status": True, "message": "Product added"})
    except:
        return  json.dumps({"status": False, "message": "try again"})


def update_product_db(product_id,prodauctname,product_price,productcategory_id):
    product = Product.query.get(product_id)
    product.prodauctname = prodauctname
    product.product_price = product_price
    product.productcategory_id = productcategory_id
    
    try:
        db.session.commit()
        return json.dumps({"status": True, "message": "product updated"})
    except:
        return json.dumps({"status": False, "message": "Try again"})


def delete_product_db(product_id):
    product = product.query.get(product_id)
    try:
        db.session.delete(product)
        db.session.commit()
        return json.dumnps({"status": True, "message": "Product deleted"})
    except:
        return json.dumps({"status": False, "message": "Try again"})
