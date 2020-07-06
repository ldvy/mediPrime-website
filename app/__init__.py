from flask import Flask
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
