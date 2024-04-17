import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from config import db
from utils import current_date


class Journal(db.Model):
    __tablename__ = "journals"
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    category = db.Column(db.String, default="publication")
    date = db.Column(db.DateTime, default=current_date())
