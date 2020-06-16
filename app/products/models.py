from app import db


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
    catalog_id = db.Column(db.Integer, db.ForeignKey('Catalog.id'), nullable=False)
    items = db.relationship("Item", backref='category', lazy=True)

    def __repr__(self):
        return f"<Category {self.name}>"


class Item(db.Model):
    __tablename__ = "Item"

    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column("Name", db.String(80), unique=True, nullable=False)
    logo = db.Column("Logo", db.BLOB)
    product_picture = db.Column("Product picture", db.BLOB)
    description = db.Column("Description", db.String(500), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('Category.id'), nullable=False)
    # I didn't add video and reviews because I didn't know for sure if it's need to be added.

    def __repr__(self):
        return f"<Item {self.model_name}>"
