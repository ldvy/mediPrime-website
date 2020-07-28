from . import bp
from app.home.models import Slider, Novation
from app.company.models import Brand
from app.news.models import NewsOn
from app.products.models import Catalog, Category
from flask import render_template, redirect, url_for, current_app, session, request


@bp.route('/')
@bp.route('/home')
def home_view():
    slides = Slider.query.order_by(Slider.slide_order_number).all()
    brands = Brand.query.all()
    news = (NewsOn.query.all())[0:6]
    novations = Novation.query.all()
    catalogs = Catalog.query.all()
    categories = Category.query.all()
    return render_template('home/index.html', slides=slides, brands=brands, news=news, novations=novations,
                           catalogs=catalogs, categories=categories)


@bp.route('/<language>')
def change_language(language):
    if language in current_app.config['LANGUAGES']:
        session['lang'] = language
    return redirect(url_for(session['url']))
