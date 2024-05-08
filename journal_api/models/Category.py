import uuid
from config import db
from models.Journal import Journal

class Category(db.Model):
    __tablenames__ = "categories"
    id = db.Column(db.String(36), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String, nullable=False, default="publication")
    journals = db.relationship(
        Journal,
        backref="category",
        cascade="all, delete, delete-orphan",
        single_parent=True,
    )