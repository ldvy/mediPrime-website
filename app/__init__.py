from flask import Flask, request, current_app, session
from flask_babelex import Babel
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
import app
import os


# Initialization for db, migrate and login flask extensions
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
mail = Mail()
babel = Babel()

# Static folder path
static_folder = os.path.join(os.path.dirname(__file__), 'static')

def create_app(config_class=Config):

    """
    Using application factory pattern for a better design purposes that includes
    troubleshooting, testing and debuging our application throw multiple instances
    of it.

    """

    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config_class)

    from app.admin_panel import admin
    admin.init_app(app)

    configure_extensions(app)
    configure_jinja_globals(app)
    configure_blueprints(app)

    return app


def configure_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)
    babel.init_app(app)


def configure_jinja_globals(app):
    app.jinja_env.globals.update(model_localisation=model_localisation)
    app.jinja_env.globals.update(set_session_url=set_session_url)


def configure_blueprints(app):
    blueprints = get_blueprints()
    for bp in blueprints:
        app.register_blueprint(bp)


@babel.localeselector
def get_locale():
    """
    Fuction that changing language of application by session key 'lang'
    """
    override = request.args.get('lang')

    if override:
        session['lang'] = override

    return session.get('lang', 'uk')


def model_localisation(object, instance_name):
    """
    Fuction that calling collumn from model by its lang representation (ru, uk)
    """
    data = getattr(object, f'{instance_name}_{get_locale()}')
    if data == None:
        return getattr(object, instance_name)
    return data


def set_session_url(url=None):
    """
    Function that handle storing current template endpoint for home.change_language
    """
    session['url'] = url
    return ''


def get_blueprints():
    return [app.company.bp, app.home.bp, app.news.bp, app.products.bp]
