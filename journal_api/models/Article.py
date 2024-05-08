import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from config import db

class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.String(36), primary_key=True, default=uuid.uuid4)
    author_id = db.Column(db.String, db.ForeignKey("authors.id"))
    journal_id = db.Column(db.String, db.ForeignKey("journals.id"))
    title = db.Column(db.String, nullable=False)
    submission_date = db.Column(db.String, default=datetime.now())
    status = db.Column(db.String, default="submitted")
