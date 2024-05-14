import uuid
import datetime
from App.extension import db
import utils



class Booking(db.Model):
    __tablename__ = "bookings"
    id = db.Column(db.String(36), primary_key=True, default=uuid.uuid4)
    created_at = db.Column(db.Date, nullable=False, default=utils.current_date())
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    num_nights = db.Column(db.Integer, nullable=False)
    nuGuest = db.Column(db.Integer, nullable=False)
    cabin_price = db.Column(db.Float, nullable=False)   
    extras_price = db.Column(db.Float, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String, nullable=False)
    has_breakfast = db.Column(db.Boolean, nullable=False, default=True)
    is_paid = db.Column(db.Boolean, nullable=False, default=False)
    observations = db.Column(db.String, nullable=True)
    cabin_id = db.Column(db.String, db.ForeignKey("cabins.id"), nullable=False)
    guest_id = db.Column(db.String, db.ForeignKey("guests.id"), nullable=False)
    
    