from flask import Flask
from flask import Blueprint

home = Blueprint('home', __name__)

#temporary function to test
@home.route('/', methods=['GET'])
def home_page():
    return "Home"