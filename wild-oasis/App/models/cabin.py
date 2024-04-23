import uuid
from App.extension import db
from utils import current_date


class Cabin(db.Model):
    __tablename__ = "cabins"
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    name = db.Column(db.String, nullable=False, unique=True)
    maxCapacity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Float, nullable=False)
    created_on = db.Column(db.DateTime, default=current_date())

    def __init__(self, name, maxCapacity, price, discount, image):
        self.name = name
        self.maxCapacity = maxCapacity
        self.price = price
        self.discount = discount
        self.image = image
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.update(self)

    def delete(self):
        db.session.delete(self)
        db.session.commit()