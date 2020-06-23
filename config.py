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
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = 1
    SQLALCHEMY_ECHO = True
    FLASK_ADMIN_SWATCH = 'readable'
