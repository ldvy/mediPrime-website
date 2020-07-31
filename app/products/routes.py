from flask import render_template, redirect, url_for, request
from . import bp
from .models import Catalog, Category, Model, Reagent, ReagentSubsection, Review
from app import db


@bp.route('/products/<catalog_name>')
def catalog_view(catalog_name):
    catalogs = Catalog.query.all()
    categories = Category.query.all()
    reag_subs = ReagentSubsection.query.all()
    cur_catalog = Catalog.query.filter(Catalog.name == catalog_name).first()
    cur_categories = Category.query.filter(Category.catalog_id == cur_catalog.id).all()
    cur_reag_subs = ReagentSubsection.query.filter(ReagentSubsection.catalog_id == cur_catalog.id).all()
    return render_template('products/catalog.html', catalogs=catalogs, categories=categories, reag_subs=reag_subs,
                           cur_catalog=cur_catalog, cur_categories=cur_categories, cur_reag_subs=cur_reag_subs)


@bp.route('/products/<catalog_name>/<category_name>')
def category_view(catalog_name, category_name):
    catalogs = Catalog.query.all()
    categories = Category.query.all()
    reag_subs = ReagentSubsection.query.all()
    cur_category = Category.query.filter(Category.name == category_name).first()
    models = Model.query.filter(Model.category_id == cur_category.id).all()
    return render_template('products/category-items.html', catalogs=catalogs, categories=categories, reag_subs=reag_subs,
                           cur_category=cur_category, catalog_name=catalog_name, models=models)


@bp.route('/products/<catalog_name>/<category_name>/<model_name>', methods=['POST', 'GET'])
def model_view(catalog_name, category_name, model_name):
    catalogs = Catalog.query.all()
    categories = Category.query.all()
    reag_subs = ReagentSubsection.query.all()
    model = Model.query.filter(Model.model_name == model_name).first()
    if request.method == 'POST':
        review_author = request.form['review_author']
        review_text = request.form['review_text']
        new_review = Review(review_author=review_author, review_text=review_text, model_id=model.id)
        try:
            db.session.add(new_review)
            db.session.commit()
        except:
            return "Could not connect to database!"
    reviews = Review.query.filter(Review.model_id == model.id).order_by(Review.review_date.desc()).all()
    return render_template('products/model.html', catalogs=catalogs, categories=categories, reag_subs=reag_subs,
                           catalog_name=catalog_name, category_name=category_name, model=model, reviews=reviews)


@bp.route('/products/<catalog_name>/reagents/<reag_subs_name>')
def reagents_view(catalog_name, reag_subs_name):
    catalogs = Catalog.query.all()
    categories = Category.query.all()
    reag_subs = ReagentSubsection.query.all()
    cur_reag_subs = ReagentSubsection.query.filter(ReagentSubsection.section_name == reag_subs_name).first()
    reagents = Reagent.query.filter(Reagent.subsection_id == cur_reag_subs.id).all()
    return render_template('products/reagents.html', catalogs=catalogs, categories=categories, reag_subs=reag_subs,
                           cur_reag_subs=cur_reag_subs, reagents=reagents, catalog_name=catalog_name)
