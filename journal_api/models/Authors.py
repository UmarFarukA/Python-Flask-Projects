import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from config import db
from models.Article import Article
from models.Journal import Journal

class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.String(36), primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False, default="author")
    articles = db.relationship(
        Article,
        backref="author",
        cascade="all, delete, delete-orphan",
        single_parent=True,
    )
    journals = db.relationship(
        Journal,
        backref="author",
        cascade="all, delete, delete-orphan",
        single_parent=True
    )

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

