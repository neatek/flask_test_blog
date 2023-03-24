from flask_combo_jsonapi import ResourceDetail, ResourceList
from app.schemas import TagSchema
from app.models.database import db
from app.models import Tag

class TagList(ResourceList):
    schema = TagSchema
    data_layer = {
        "session": db.session,
        "model": Tag,
    }

class TagDetail(ResourceDetail):
    schema = TagSchema
    data_layer = {
        "session": db.session,
        "model": Tag,
    }
