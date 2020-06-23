from app import db
from datetime import datetime
from sqlalchemy.types import ARRAY


"""

Designing models using SQLalchemy
Models that is responsible for "News category" on web application

"""
class NewsCategory(db.Model):
    __tablename__ = 'NewsCategory'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    news_list = db.relationship("NewsOn", backref='category', lazy=True)

    def __repr__(self):
        return f"<NewsCategory {self.name}>"


# This model is not fully responsible for application | Delete soon | TBD
class NewsOn(db.Model):
    __tablename__ = 'NewsOn'

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('NewsCategory.id'))
    title = db.Column("Title", db.String(80), unique=True, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    preview_image = db.Column(db.Unicode(128), nullable=True)
    text = db.Column(db.TEXT)
    images = db.Column('Images', ARRAY(db.Unicode(128)), nullable=True)

    def __repr__(self):
        return f"<News {self.title}>"
