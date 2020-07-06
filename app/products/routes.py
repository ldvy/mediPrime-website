from flask import render_template, redirect, url_for
from . import bp
from .models import Catalog, Category, Model, Reagent, ReagentSubsection


@bp.route('/products/')
def product_view():
    all_catalogs = Catalog.query.all()
    return render_template('products/products.html', catalogs=all_catalogs)


@bp.route('/products/<category>')
def category_view(category):
    category = Category.query.filter_by(name=category).first()
    return render_template('products/category.html', category=category)


@bp.route('/products/<category>/<model>')
def model_view(category, model):
    model = Model.query.filter_by(model_name=model).first()
    return render_template('products/model.html', model=model)


@bp.route('/products/reagents/')
def reagent_category_view():
    categories = ReagentSubsection.query.all()
    return render_template('products/reagents.html', categories=categories)


@bp.route('/products/reagents/<category_name>')
def reagents_view(category_name):
    category = ReagentSubsection.query.filter_by(section_name=category_name).first()
    return render_template('products/reagent.html', category=category)
