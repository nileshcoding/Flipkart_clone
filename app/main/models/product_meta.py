from app.main.settings import db
from . import ProductModel


class Productmeta(db.model):
    id=db.Column(db.Integer,primary_key=True)
    image_path=db.Column(db.String(100),nullable = False)
    product_id=db.Column(db.Integer, db.ForeignKey('product.id'))
