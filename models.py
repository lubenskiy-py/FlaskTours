from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tur(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, default="https://picsum.photos/200/300?grayscale", nullable=False)
    is_booked = db.Column(db.Boolean, default=False)