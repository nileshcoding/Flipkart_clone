from app.main.settings import db
from . import UserModel


class UserAddress(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    address = db.Column(db.String(250),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False,Unique=True)