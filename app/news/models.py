from app import db
from datetime import datetime
from sqlalchemy.types import ARRAY


"""

Designing models using SQLalchemy
Models that is responsible for "News category" on web application

"""
# This model is not fully responsible for application | Delete soon | TBD
class NewsOn(db.Model):
    __tablename__ = 'NewsOn'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column("Title", db.String(80), unique=True, nullable=False)
    title_ru = db.Column("Title RU", db.String(80))
    title_uk = db.Column("Title UK", db.String(80))
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    preview_image = db.Column(db.Unicode(128), nullable=True)
    text = db.Column('Text', db.TEXT)
    text_ru = db.Column('Text RU', db.TEXT)
    text_uk = db.Column('Text UK', db.TEXT)

    def __repr__(self):
        return f"<News {self.title}>"
