from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

static_folder = os.path.join(os.path.dirname(__file__), 'static')

def create_app(config_class=Config):
    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    from app.admin_panel import admin
    admin.init_app(app)

    from app.home import bp as bp_home
    app.register_blueprint(bp_home)

    from app.products import bp as bp_products
    app.register_blueprint(bp_products)

    return app


from app.products import models as product_models
from app.admin_panel import models as admin_models
