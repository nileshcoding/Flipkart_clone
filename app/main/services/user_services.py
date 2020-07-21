from app.main.settings import db
from app.main.models import UserModel

def add_user(name,email,password,role):
    user = User(name=name, email=email, password=password, role=role)
    db.session.add(user)
    db.session.commit()