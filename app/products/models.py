from app import db
from sqlalchemy.dialects.postgresql import JSON, ARRAY
from sqlalchemy_utils.types import URLType
from datetime import datetime


"""

Designing models using SQLalchemy
Models that is responsible for "Jobs category" on web application

"""
class Catalog(db.Model):
    __tablename__ = "Catalog"

    id = db.Column(db.Integer, primary_key=True)
    cat_img = db.Column("Image", db.Unicode(128), nullable=False)
    name = db.Column("Name", db.String(80), unique=True, nullable=False)
    name_ru = db.Column("Name RU", db.String(80), unique=True)
    name_uk = db.Column("Name UK", db.String(80), unique=True)
    categories = db.relationship("Category", backref='catalog', lazy=True)
    reagent_subs = db.relationship("ReagentSubsection", backref='catalog', lazy=True)

    def __repr__(self):
        return f"<Catalog {self.name}>"


class Category(db.Model):
    __tablename__ = "Category"

    id = db.Column(db.Integer, primary_key=True)
    cat_img = db.Column("Image", db.Unicode(128), nullable=False)
    name = db.Column("Name", db.String(80), unique=True, nullable=False)
    name_ru = db.Column("Name RU", db.String(80), unique=True)
    name_uk = db.Column("Name UK", db.String(80), unique=True)
    catalog_id = db.Column(db.Integer, db.ForeignKey('Catalog.id'))
    models = db.relationship("Model", backref='category', lazy=True)

    def __repr__(self):
        return f"<Category {self.name}>"


class Model(db.Model):
    __tablename__ = "Model"

    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column("Name", db.String(80), unique=True, nullable=False)
    model_name_ru = db.Column("Name RU", db.String(80), unique=True)
    model_name_uk = db.Column("Name UK", db.String(80), unique=True)
    logo = db.Column("Logo", db.Unicode(128))
    product_picture = db.Column('Product picture', ARRAY(db.Unicode(128)))
    description = db.Column("Description", db.TEXT, nullable=False)
    description_ru = db.Column("Description RU", db.TEXT)
    description_uk = db.Column("Description UK", db.TEXT)
    characteristics = db.Column("Characteristics", ARRAY(db.String))
    characteristics_ru = db.Column("Characteristics RU", ARRAY(db.String))
    characteristics_uk = db.Column("Characteristics UK", ARRAY(db.String))
    category_id = db.Column(db.Integer, db.ForeignKey('Category.id'))
    country = db.Column('Country', db.String(80))
    country_ru = db.Column('Country RU', db.String(80))
    country_uk = db.Column('Country UK', db.String(80))
    brand = db.Column('Brand', db.String(80))
    brand_ru = db.Column('Brand RU', db.String(80))
    brand_uk = db.Column('Brand UK', db.String(80))
    video_link = db.Column('Video link', URLType)
    reviews = db.relationship("Review", backref="model", lazy=True)

    def __repr__(self):
        return f"<Item {self.model_name}>"


# hardcoded model for representation of reagents
class ReagentSubsection(db.Model):
    __tablename__ = "ReagentSubsection"

    id = db.Column(db.Integer, primary_key=True)
    sec_img = db.Column("Image", db.Unicode(128), nullable=False)
    section_name = db.Column("Name", db.String(80), unique=True, nullable=False)
    section_name_ru = db.Column("Name RU", db.String(80))
    section_name_uk = db.Column("Name Uk", db.String(80))
    catalog_id = db.Column(db.Integer, db.ForeignKey('Catalog.id'))
    reagents = db.relationship("Reagent", backref="subsection", lazy=True)

    def __repr__(self):
        return f"<ReagentSubsection {self.section_name}>"


class Reagent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subsection_id = db.Column(db.Integer, db.ForeignKey('ReagentSubsection.id'))
    reagent_name = db.Column("Name", db.String(80), unique=True, nullable=False)
    reagent_name_ru = db.Column("Name Uk", db.String(80))
    reagent_name_uk = db.Column("Name RU", db.String(80))
    method = db.Column("Method", db.String(200), unique=True, nullable=False)
    method_ru = db.Column("Method RU", db.String(200))
    method_uk = db.Column("Method Uk", db.String(200))
    description = db.Column("Description", ARRAY(db.String))
    description_ru = db.Column("Description RU", ARRAY(db.String))
    description_uk = db.Column("Description UK", ARRAY(db.String))
    # Using sqlalchemy.dialects.types.JSON for representing Json in postgresql
    json_dc = db.Column("DistributionCode", JSON, nullable=False)

    def __repr__(self):
        return f"<Reagent {self.reagent_name}>"


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model_id = db.Column(db.Integer, db.ForeignKey('Model.id'))
    review_author = db.Column("Review author", db.String(40), nullable=False)
    review_text = db.Column("Review text", db.String(600), nullable=False)
    review_date = db.Column("Review date", db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<Review {self.review_author}>"
