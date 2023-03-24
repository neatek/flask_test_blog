from flask_combo_jsonapi import ResourceDetail, ResourceList
from app.schemas import ArticleSchema
from app.models.database import db
from app.models import Article


class ArticleList(ResourceList):
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article,
    }


class ArticleDetail(ResourceDetail):
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article,
    }
