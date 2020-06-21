from flask import Blueprint


bp = Blueprint("Jobs", __name__)


from . import routes
