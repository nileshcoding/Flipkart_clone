from app.main.settings import db
from . import UserModel,ProductModel

class Comments(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

class CommentDetail(db.Model):
    __tablename__ = 'comment_user'
    id = db.Column(db.Integer,primary_key=True)
    product_id = db.Column(db.Integer,db.ForeignKey('product.id'),nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'), unique=True, nullable=False)
    upvote = db.Column(db.Integer,nullable=True)
    downvote=db.Column(db.Integer,nullable=True)
