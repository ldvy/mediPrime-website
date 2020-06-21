from app import db


# Model for slider
class Slider(db.Model):
    __tablename__ = "Slider"

    id = db.Column(db.Integer, primary_key=True)
    bg_image = db.Column("Background", db.Unicode(128), nullable=False)
    title = db.Column("Title", db.String(80), unique=True, nullable=False)
    text = db.Column("Text", db.TEXT, unique=True, nullable=False)
    btn_link = db.Column("Link", db.Unicode(128), default="#")
    slide_order_number = db.Column(db.Integer)

    def __repr__(self):
        return f"<Slider {self.title}>"
