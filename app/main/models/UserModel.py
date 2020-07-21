from app.main.settings import db

class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False,unique = True)
    password = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(100), nullable=False)