from app.main.settings import db
from . import ProductModel,UserModel

class Cart(db.Model):
    __tablename__='cart'
    id=db.Column(db.Integer, primary_key=True)
    quantity=db.Column(db.Integer,nullable=False)
    total_cost=db.Column(db.Integer,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    product_id=db.Column(db.Integer,db.ForeignKey('product.id'))
