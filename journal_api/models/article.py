import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from config import db

class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    user_id = db.Column(db.String, db.ForeignKey("users.id"))
    title = db.Column(db.String, nullable=False)
    submission_date = db.Column(db.String, default=datetime.now())
    status = db.Column(db.String, default="submitted")
