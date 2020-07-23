from flask import Flask
from flask import Blueprint
from flask import request
from app.main.settings import db
from app.main.routes.home import *
from app.main.routes.user import *
from app.main.routes.product import *
from app.main.routes.login import *
from app.main.routes.search import *
from app.main.routes.cart import *
from app.main.routes.order import *


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Anton@123@localhost/flipkart_db"
    db.init_app(app)

    app.register_blueprint(login, url_prefix='/login')
    app.register_blueprint(home, url_prefix='/home')
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(products, url_prefix='/products')
    app.register_blueprint(search, url_prefix='/search')
    app.register_blueprint(cart, url_prefix='/cart')
    app.register_blueprint(order, url_prefix='/order')

    return app