from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.home import bp as bp_home
    app.register_blueprint(bp_home)

    from app.products import bp as bp_products
    app.register_blueprint(bp_products)

    return app


from app.products import models
