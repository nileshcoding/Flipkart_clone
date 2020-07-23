from app.main.settings import db
from app.main.models.OrderModel import *
from app.main.models.ProductModel import *
from app.main.models.UserModel import *
from sqlalchemy import text


def get_my_orders_db(user_id):
    sql = text('SELECT product.product_name,product.product_price,orders.* FROM orders JOIN order_product on order_product.order_id=orders.id JOIN product ON product.id=order_product.product_id WHERE orders.user_id = :user_id;')    
    data = db.engine.execute(sql,{'user_id': user_id})
    result = data.fetchall()
    li_result = []
    for row in result:
        li_result.append(str(row))
    return li_result 


def place_order_db(user_id,product_id):
    product = Product.query.get(product_id)
    user = User.query.get(user_id)
    order = Orders(amount=product.product_price,shipment='in 2 to 3 days',ship_address=user.address,user_id=user_id)
    db.session.add(order)
    db.session.commit()
    order_id = order.id

    order_product = OrderProduct(order_id=order_id, product_id=product_id)
    db.session.add(order_product)
    db.session.commit()
