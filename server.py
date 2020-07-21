from app.main import create_app
from app.main.settings import db
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.main.models import *

app = create_app()

migrate = Migrate(app,db)

if __name__ == 'main':
    app.run()