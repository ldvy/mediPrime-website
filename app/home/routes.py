from . import bp
from flask import render_template
from app.products.models import Catalog


@bp.route('/')
def home_view():
    return render_template('home/index.html')
