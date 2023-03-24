from flask_combo_jsonapi import ResourceDetail, ResourceList
from app.schemas import AuthorSchema
from app.models.database import db
from app.models import Author
from app.models import Author, Article
from combojsonapi.event.resource import EventsResource


class AuthorDetailEvents(EventsResource):
    def event_get_articles_count(self, **kwargs):
        return {
            "count": Article.query.filter(Article.author_id == kwargs["id"]).count()
        }


class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
        "session": db.session,
        "model": Author,
    }


class AuthorDetail(ResourceDetail):
    schema = AuthorSchema
    events = AuthorDetailEvents
    data_layer = {
        "session": db.session,
        "model": Author,
    }
