from flask import Flask
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.home import bp as bp_home
    app.register_blueprint(bp_home)

    return app
