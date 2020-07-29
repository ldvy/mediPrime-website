from . import bp
from app.news.models import NewsOn
from app.products.models import Catalog, Category, ReagentSubsection
from flask import render_template, redirect, url_for, current_app, session, request
from config import NEWS_POSTS_PER_PAGE


@bp.route('/news')
@bp.route('/news/<int:page>')
def news_list(page=1):
    catalogs = Catalog.query.all()
    categories = Category.query.all()
    reag_subs = ReagentSubsection.query.all()
    posts = NewsOn.query.paginate(page, NEWS_POSTS_PER_PAGE, False)
    return render_template('news/news_list.html', catalogs=catalogs, categories=categories, reag_subs=reag_subs
                           , posts=posts, cur_page=page)


@bp.route('/news/<int:page>/<title>')
def news_post(page, title):
    catalogs = Catalog.query.all()
    categories = Category.query.all()
    reag_subs = ReagentSubsection.query.all()
    post = NewsOn.query.filter(NewsOn.title == title).first()
    latest_posts = NewsOn.query.order_by(NewsOn.pub_date.desc())[0:3]
    return render_template('news/news_post.html', catalogs=catalogs, categories=categories, reag_subs=reag_subs,
                           cur_page=page, post=post, latest_posts=latest_posts)


