import uuid
import datetime
from App.extension import db
from utils import current_date

class Setting(db.Model):
    __tablename__ = "settings"
    id = db.Column(db.String(36), primary_key = True, default=uuid.uuid4)
    created_at = db.Column(db.DateTime, nullable=False, default=current_date())
    num_booking_length = db.Column(db.Integer, nullable=False)
    max_guests_book = db.Column(db.Integer, nullable=False)
    breakfast_price = db.Column(db.Float, nullable=False)