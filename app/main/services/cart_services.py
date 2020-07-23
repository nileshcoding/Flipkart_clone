from app.main.settings import db
import json
from app.main.models.CartModel import *
from sqlalchemy import text
from app.main.models.ProductModel import *


def get_my_cart(user_id):
    sql = text('SELECT product.product_name as pn, cart.quantity as cq, cart.total_cost as ct FROM cart JOIN product ON product.id = cart.product_id WHERE cart.user_id=:user_id;')
    data = db.engine.execute(sql,{"user_id": user_id})
    result = data.fetchall()
    li_result = []
    for row in result:
        li_result.append([row.pn,row.cq,row.ct])
    return result


def add_to_cart_db(user_id,product_id):
    existing_cart = Cart.query.filter_by(user_id=user_id, product_id= product_id).first()
    product = Product.query.get(product_id)
    if existing_cart is not None:
        new_quantity = int(existing_cart.quantity) + 1
        new_total_cost = existing_cart.total_cost + product.product_price
        existing_cart.total_cost = new_total_cost
        existing_cart.quantity = new_quantity
        db.session.commit()
    else:
        new_quantity = 1
        new_total_cost = product.product_price
        cart_value = Cart(new_quantity,new_total_cost,user_id,product_id)
        db.session.add(cart_value)
        db.session.commit()