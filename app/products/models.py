from app import db
from sqlalchemy.dialects.postgresql import JSON


"""

Designing models using SQLalchemy
Models that is responsible for "Jobs category" on web application

"""
class Catalog(db.Model):
    __tablename__ = "Catalog"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("Name", db.String(80), unique=True, nullable=False)
    categories = db.relationship("Category", backref='catalog', lazy=True)

    def __repr__(self):
        return f"<Catalog {self.name}>"


class Category(db.Model):
    __tablename__ = "Category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("Name", db.String(80), unique=True, nullable=False)
    catalog_id = db.Column(db.Integer, db.ForeignKey('Catalog.id'))
    models = db.relationship("Model", backref='category', lazy=True)

    def __repr__(self):
        return f"<Category {self.name}>"


class Model(db.Model):
    __tablename__ = "Model"

    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column("Name", db.String(80), unique=True, nullable=False)
    logo = db.Column("Logo", db.Unicode(128))
    product_picture = db.Column("Product picture", db.Unicode(128))
    description = db.Column("Description", db.TEXT, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('Category.id'))
    # I didn't add video and reviews because I didn't know for sure if it's need to be added.

    def __repr__(self):
        return f"<Item {self.model_name}>"


# hardcoded model for representation of reagents
class ReagentSubsection(db.Model):
    __tablename__ = "ReagentSubsection"

    id = db.Column(db.Integer, primary_key=True)
    section_name = db.Column("Name", db.String(80), unique=True, nullable=False)
    reagents = db.relationship("Reagent", backref="subsection", lazy=True)


class Reagent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subsection_id = db.Column(db.Integer, db.ForeignKey('ReagentSubsection.id'))
    reagent_name = db.Column("Name", db.String(80), unique=True, nullable=False)
    method = db.Column("Method", db.String(200), unique=True, nullable=False)
    # Using sqlalchemy.dialects.types.JSON for representing Json in postgresql
    json_dc = db.Column("DistributionCode", JSON, nullable=False)

    def __repr__(self):
        return f"<Reagent {self.reagent_name}>"
