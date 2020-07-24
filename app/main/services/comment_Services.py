from app.main.settings import db
import json
from app.main.models.CommentModel import *


def get_comments_db(product_id):
    comments = Comments.query.all()
    li_result = []
    for row in comments:
        li_result.append(str(row))
    return li_result