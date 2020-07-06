from flask import Blueprint


bp = Blueprint("company", __name__)


from . import routes
