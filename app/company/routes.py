from . import bp
from .models import Job, Brand, Service
from flask import render_template


@bp.route('/company/')
def company_view():
    jobs = Job.query.all()
    brands = Brand.query.all()
    return render_template('company/company.html', jobs=jobs, brands=brands)


@bp.route('/services/')
def services_view():
    services = Service.query.all()
    return render_template('company/services.html', services=services)
