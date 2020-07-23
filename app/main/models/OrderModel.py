from app.main.settings import db
from . import UserModel,ProductModel

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer,nullable = False)
    shipment = db.Column(db.String(100),nullable = False)
    ship_address = db.Column(db.String(100),nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class OrderProduct(db.Model):
    _tablename__='order_product'
    id=db.Column(db.Integer, primary_key=True)
    order_id=db.Column(db.Integer, db.ForeignKey('orders.id'))
    product_id=db.Column(db.Integer, db.ForeignKey('product.id'))
