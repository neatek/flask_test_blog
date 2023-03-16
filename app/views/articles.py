from flask import Blueprint, render_template, request, current_app, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound
from app.models.database import db
from app.models import Author, Article, Tag
from app.forms.article import CreateArticleForm

articles_app = Blueprint("articles_app", __name__)


@articles_app.route("/", endpoint="list")
def articles_list():
    articles = Article.query.all()
    return render_template("articles/list.html", articles=articles)


@articles_app.route("/<int:article_id>/", endpoint="details")
def article_detals(article_id):
    article = (
        Article.query.filter_by(id=article_id)
        .options(joinedload(Article.tags))  # подгружаем связанные теги!
        .one_or_none()
    )
    if article is None:
        raise NotFound
    return render_template("articles/details.html", article=article)


@articles_app.route("/create/", methods=["GET", "POST"], endpoint="create")
@login_required
def create_article():
    error = None
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by("name")]
    if request.method == "POST" and form.validate_on_submit():
        if not current_user.author:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.commit()

        article = Article(
            title=form.title.data.strip(),
            body=form.body.data,
            author=current_user.author,
        )
        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                article.tags.append(tag)
        db.session.add(article)

        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create a new article!")
            error = "Could not create article!"
        else:
            return redirect(url_for("articles_app.details", article_id=article.id))
    return render_template("articles/create.html", form=form, error=error)
