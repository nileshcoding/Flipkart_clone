from app.main.settings import db
from . import UserModel


class WishlistModel(db.Model):
    __tablename__='Mywhislist'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

