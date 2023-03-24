from flask_combo_jsonapi import ResourceDetail, ResourceList
from app.schemas import UserSchema
from app.models.database import db
from app.models import User
from app.permissions.user import UserPermission


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
        "permission_get": [UserPermission],
    }
