import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from config import db
from utils import current_date
from models.Article import Article


class Journal(db.Model):
    __tablename__ = "journals"
    id = db.Column(db.String(36), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String, nullable=False)
    author_id = db.Column(db.String, db.ForeignKey("authors.id"))
    category_id = db.Column(db.String, db.ForeignKey("categories.id"))
    articles = db.relationship(
        Article,
        backref="journal",
        cascade="all, delete, delete-orphan",
        single_parent=True,
    )
    date = db.Column(db.DateTime, default=current_date())
    
