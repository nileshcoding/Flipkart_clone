from app.main.settings import db
from . import CategoriesModel

class ProductModel(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    product_name=db.Column(db.String(100), nullable = False)
    product_price=db.Column(db.Float, nullable=False)
    product_category_id=db.Column(db.Integer, db.ForeignKey('category.id'))
