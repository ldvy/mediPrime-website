import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    """
    Configuration class that will be used in application factory pattern.
    app.config.from_object(ConfigClass)
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(16)
    DEBUG = 1
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    FLASK_ADMIN_SWATCH = 'readable'

    # localization
    LANGUAGES = ['ru', 'uk']
    BABEL_DEFAULT_LOCALE = 'uk'

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
