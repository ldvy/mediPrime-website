import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "1q2w3e4r5t6y7u8i9o0p"
    SQLALCHEMY_DATABASE_URI = 'postgresql:///mediprime'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = 1
    SQLALCHEMY_ECHO = True
    FLASK_ADMIN_SWATCH = 'readable'
