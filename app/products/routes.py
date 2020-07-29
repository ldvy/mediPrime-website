from flask import render_template, redirect, url_for
from . import bp
from .models import Catalog, Category, Model, Reagent, ReagentSubsection


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


# @bp.route('/products/<category>/<model>')
# def model_view(category, model):
#     model = Model.query.filter_by(model_name=model).first()
#     return render_template('products/model.html', model=model)
#
#
# @bp.route('/products/reagents/')
# def reagent_category_view():
#     categories = ReagentSubsection.query.all()
#     return render_template('products/reagents.html', categories=categories)
#
#
# @bp.route('/products/reagents/<category_name>')
# def reagents_view(category_name):
#     category = ReagentSubsection.query.filter_by(section_name=category_name).first()
#     return render_template('products/reagent.html', category=category)
