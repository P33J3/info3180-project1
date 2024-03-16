from . import db


class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    location = db.Column(db.String(80))
    price = db.Column(db.Integer)
    type = db.Column(db.String(80))
    description = db.Column(db.String(250))
    photo_filename = db.Column(db.String(160))

    def __init__(self, title, bedrooms, bathrooms, location, price, type, description, photo_filename):
        self.title = title
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.location = location
        self.price = price
        self.type = type
        self.description = description
        self.photo_filename = photo_filename

    def __repr__(self):
        return '<Property %r>' % self.title
