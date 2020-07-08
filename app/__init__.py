from flask import Flask, request, current_app, session
from flask_babel import Babel
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
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

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)
    babel.init_app(app)

    app.jinja_env.globals.update(model_localisation=model_localisation)
    app.jinja_env.globals.update(set_session_url=set_session_url)

    from app.admin_panel import admin
    admin.init_app(app)

    from app.home import bp as bp_home
    app.register_blueprint(bp_home)

    from app.products import bp as bp_products
    app.register_blueprint(bp_products)

    from app.company import bp as bp_company
    app.register_blueprint(bp_company)

    from app.news import bp as bp_news
    app.register_blueprint(bp_news)

    return app


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
    try:
        return getattr(object, f'{instance_name}_{get_locale()}')
    except:
        return getattr(object, instance_name)


def set_session_url(url=None):
    """
    Function that handle storing current template endpoint for home.change_language
    """
    session['url'] = url
    return ''
