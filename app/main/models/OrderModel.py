from app.main.settings import db
from . import UserModel,ProductModel

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    paid = db.Column(db.Boolean,nullable=False)
    payment_id = db.Column(db.Integer,db.ForeignKey('payment.id'), unique=True, nullable=False)

class OrderDetail(db.Model):
    _tablename__='order_detail'
    id=db.Column(db.Integer, primary_key=True)
    order_id=db.Column(db.Integer, db.ForeignKey('orders.id'))
    product_id=db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer,nullable=False)
    amount = db.Column(db.Integer,nullable = False)
    ship_address = db.Column(db.String(100),nullable = False)
