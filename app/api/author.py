from flask_combo_jsonapi import ResourceDetail, ResourceList
from app.schemas import AuthorSchema
from app.models.database import db
from app.models import Author


class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
        "session": db.session,
        "model": Author,
    }


class AuthorDetail(ResourceDetail):
    schema = AuthorSchema
    data_layer = {
        "session": db.session,
        "model": Author,
    }
