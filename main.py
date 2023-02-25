from flask import Flask
from flask import render_template
from views.users import users_app
from views.articles import articles_app


app = Flask(__name__)


app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)
