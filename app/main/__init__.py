from flask import Flask
from flask import Blueprint
from flask import request
from app.main.settings import db
#import all the blueprints from py files
from app.main.routes.home import *
from app.main.routes.user import *

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Anton@123@localhost/flipkart_db"
    db.init_app(app)

    #here goes all the blueprints
    app.register_blueprint(home, url_prefix='/home')
    app.register_blueprint(user, url_prefix='/user')
    
    return app