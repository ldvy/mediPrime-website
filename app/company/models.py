from app import db
from sqlalchemy.types import ARRAY

"""

Designing models using SQLalchemy
Models that is responsible for "Jobs category" on web application

"""
class Job(db.Model):
    __tablename__ = "Job"

    id = db.Column(db.Integer, primary_key=True)
    position = db.Column("Position", db.String(500), nullable=False)
    position_uk = db.Column("Position RU", db.String(500))
    position_ru = db.Column("Position UK", db.String(500))
    requirements = db.Column("Requirements", ARRAY(db.String), nullable=False)
    requirements_ru = db.Column("Requirements RU", ARRAY(db.String))
    requirements_uk = db.Column("Requirements UK", ARRAY(db.String))
    responsibilities = db.Column("Responsibilities", ARRAY(db.String), nullable=False)
    responsibilities_ru = db.Column("Responsibilities RU", ARRAY(db.String))
    responsibilities_uk = db.Column("Responsibilities UK", ARRAY(db.String))
    conditions = db.Column("Conditions", ARRAY(db.String), nullable=False)
    conditions_ru = db.Column("Conditions RU", ARRAY(db.String))
    conditions_uk = db.Column("Conditions UK", ARRAY(db.String))

    def __repr__(self):
        return f"<Job {self.position}>"


class Service(db.Model):
    __tablename__ = "Service"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column("Title", db.String(400), nullable=False)
    title_ru = db.Column("Title RU", db.String(400))
    title_uk = db.Column("Title UK", db.String(400))
    icon = db.Column("Icon", db.String(150), nullable=False)
    text = db.Column("Text", db.TEXT, nullable=False)
    text_ru = db.Column("Text RU", db.TEXT)
    text_uk = db.Column("Text UK", db.TEXT)

    def __repr__(self):
        return f"<Service {self.title}>"


class Brand(db.Model):
    __tablename__ = "Brand"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("Name", db.String(100), nullable=False)
    name_ru = db.Column("Name RU", db.String(100))
    name_uk = db.Column("Name UK", db.String(100))
    description = db.Column('Description', db.TEXT)
    description_ru = db.Column('Description RU', db.TEXT)
    description_uk = db.Column('Description UK', db.TEXT)
    short_description = db.Column('Short description', db.String(200))
    short_description_ru = db.Column('Short description RU', db.String(200))
    short_description_uk = db.Column('Short description UK', db.String(200))
    country = db.Column("Country", db.String(100), nullable=False)
    country_ru = db.Column("Country RU", db.String(100))
    country_uk = db.Column("Country UK", db.String(100))
    brand_website = db.Column("Brand website", db.Unicode(128), default="#")
    logo = db.Column("Logo", db.Unicode(128), nullable=False)

    def __repr__(self):
        return f"<Brand {self.title}>"
