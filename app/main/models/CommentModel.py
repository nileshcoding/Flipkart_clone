from app.main.settings import db
from . import UserModel,ProductModel

class Comments(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key=True)
    comment=db.Column(db.String(255),nullable=False)
    upvote = db.Column(db.Integer,nullable=True)
    downvote=db.Column(db.Integer,nullable=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    product_id=db.Column(db.Integer,db.ForeignKey('product.id'))
