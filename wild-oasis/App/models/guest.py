import uuid
import datetime
from App.extension import db
from utils import current_date


class Guest(db.Model):
    __tablename__ = "guests"
    id = db.Column(db.String(36), primary_key=True, default=uuid.uuid4)
    created_at = db.Column(db.DateTime, nullable=False, default=current_date())
    email = db.Column(db.String, nullable=False)
    nationality = db.Column(db.String, nullable=False)
    country_flag = db.Column(db.String, nullable=True)
    fullName = db.Column(db.String, nullable=False)
    national_id = db.Column(db.Integer, nullable=False)
    bookings_id = db.relationship("Booking", backref="guest", lazy=True)