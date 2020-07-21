from app.main.settings import db
from . import UserModel,ProductModel

class OrderModel(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer,nullable = False)
    shipment = db.Column(db.String(100),nullable = False)
    ship_Address=db.Column(db.String(100),nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class OrderProduct(db.Model):
    _tablename__='orderproduct'
    id=db.Column(db.Integer, primary_key=True)
    order_id=db.Column(db.Integer, db.ForeignKey('order.id'))
    product_id=db.Column(db.Integer, db.ForeignKey('product.id'))
