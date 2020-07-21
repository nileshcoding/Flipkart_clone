from app.main.settings import db

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(200), unique=True, nullable=False)


class TreePath(db.Model):
    __tablename__ = 'Treepath'
    ancestor = db.Column(db.Integer,db.ForeignKey('category.id'),primary_key=True)
    descendants = db.Column(db.Integer, db.ForeignKey('category.id'),primary_key=True)
