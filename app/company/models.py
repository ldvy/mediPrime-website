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
    requirements = db.Column("Requirements", ARRAY(db.String), nullable=False)
    responsibilities = db.Column("Responsibilities", ARRAY(db.String), nullable=False)
    conditions = db.Column("Conditions", ARRAY(db.String), nullable=False)

    def __repr__(self):
        return f"<Job {self.position}>"


class Service(db.Model):
    __tablename__ = "Service"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column("Title", db.String(400), nullable=False)
    icon = db.Column("Icon", db.String(150), nullable=False)
    text = db.Column("Text", db.TEXT, nullable=False)

    def __repr__(self):
        return f"<Service {self.title}>"


class Brand(db.Model):
    __tablename__ = "Brand"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("Name", db.String(100), nullable=False)
    country = db.Column("Country", db.String(100), nullable=False)
    brand_website = db.Column("Brand website", db.Unicode(128), default="#")
    logo = db.Column("Logo", db.Unicode(128), nullable=False)

    def __repr__(self):
        return f"<Brand {self.title}>"
