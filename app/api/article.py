from flask_combo_jsonapi import ResourceDetail, ResourceList
from app.schemas import ArticleSchema
from app.models.database import db
from app.models import Article
from combojsonapi.event.resource import EventsResource


class ArticleListEvents(EventsResource):
    def event_get_count(self, _permission_user):
        return {"count": Article.query.count()}


class ArticleList(ResourceList):
    schema = ArticleSchema
    events = ArticleListEvents
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
