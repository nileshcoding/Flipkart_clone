from app.main.settings import db
from . import UserModel


class WhislistModel(db.model):
    __tablename__='Mywhislist'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100),nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
