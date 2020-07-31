from . import bp
from app.products.models import Category, Catalog, ReagentSubsection
from .models import Job, Brand, Service
from flask import render_template


@bp.route('/company/brands')
def brands_view():
    catalogs = Catalog.query.all()
    categories = Category.query.all()
    reag_subs = ReagentSubsection.query.all()
    brands = Brand.query.all()
    return render_template('company/brands.html', catalogs=catalogs, categories=categories, reag_subs=reag_subs,
                           brands=brands)


@bp.route('/services/')
def services_view():
    services = Service.query.all()
    return render_template('company/services.html', services=services)


@bp.route('/jobs/')
def jobs_view():
    catalogs = Catalog.query.all()
    categories = Category.query.all()
    reag_subs = ReagentSubsection.query.all()
    jobs = Job.query.all()
    return render_template('company/jobs.html', catalogs=catalogs, categories=categories, reag_subs=reag_subs, jobs=jobs)


@bp.route('/contacts/')
def contacts_view():
    catalogs = Catalog.query.all()
    categories = Category.query.all()
    reag_subs = ReagentSubsection.query.all()
    return render_template('company/contacts.html', catalogs=catalogs, categories=categories, reag_subs=reag_subs)


