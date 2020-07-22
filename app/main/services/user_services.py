from app.main.settings import db
from app.main.models.UserModel import User
import json

def add_user(name,email,password,role):
    user = User(name=name, email=email, password=password, role=role)
    db.session.add(user)
    db.session.commit()


def delete_user_db(user_id):
    user = User.query.get(user_id)
    try:
        db.session.delete(user)
        db.session.commit()
        return json.dumps({"status": True, "message": "user deleted"})
    except:
        return json.dumps({"status": False, "message": "Try again"})