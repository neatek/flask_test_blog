import os
from flask import Flask
from flask_migrate import Migrate
from flask import render_template
from app.views.users import users_app
from app.views.articles import articles_app
from app.views.auth import login_manager, auth_app
from app.views.authors import authors_app
from app.models.database import db
from app.admin import admin
from app.security import flask_bcrypt


app = Flask(__name__)
cfg_name = os.environ.get("CONFIG_NAME") or "DevConfig"
app.config.from_object(f"app.configs.{cfg_name}")

db.init_app(app)
login_manager.init_app(app)
migrate = Migrate(app, db)
flask_bcrypt.init_app(app)
admin.init_app(app)

app.register_blueprint(auth_app, url_prefix="/auth")
app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")
app.register_blueprint(authors_app, url_prefix="/authors")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)


# @app.cli.command("init-db")
# def init_db():
#     """
#     Run in your terminal:
#     flask init-db
#     """
#     db.create_all()
#     print("done!")


# @app.cli.command("create-users")
# def create_users():
#     """
#     Run in your terminal:
#     flask create-users
#     > done! created users: <User #1 'admin'> <User #2 'james'>
#     """
#     from models import User

#     admin = User(username="admin", is_staff=True)
#     james = User(username="james")
#     db.session.add(admin)
#     db.session.add(james)
#     db.session.commit()
#     print("done! created users:", admin, james)


@app.cli.command("create-admin")
def create_admin():
    """
    Run in your terminal:
    ➜ flask create-admin
    > created admin: <User #1 'admin'>
    """
    from app.models import User

    admin = User(username="admin", is_staff=True)
    admin.password = os.environ.get("ADMIN_PASSWORD") or "adminpass"
    db.session.add(admin)
    db.session.commit()
    print("created admin:", admin)


@app.cli.command("create-tags")
def create_tags():
    """
    Run in your terminal:
    ➜ flask create-tags
    """
    from app.models import Tag

    for name in [
        "flask",
        "django",
        "python",
        "sqlalchemy",
        "news",
    ]:
        tag = Tag(name=name)
        db.session.add(tag)
        db.session.commit()
    print("created tags")
