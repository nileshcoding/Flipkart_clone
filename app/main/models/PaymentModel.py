from app.main.settings import db
from . import UserModel

class PaymentModel(db.Model):
    __tablename__='payment'
    id = db.Column(db.Integer, primary_key=True)
    payment_type=db.Column(db.String(200), nullable=False)
    amount=db.Column(db.Integer,nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
