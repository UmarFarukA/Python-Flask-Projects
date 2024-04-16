from datetime import datetime
from config import db, ma
from models.notes import Note, NoteSchema
from marshmallow_sqlalchemy import fields

class User(db.Model):
  __tablename__ = "users"
  id = db.Column(db.Integer, primary_key=True)
  lname = db.Column(db.String(32), unique=True)
  fname = db.Column(db.String(32))
  timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
  notes = db.relationship(
    Note, 
    backref='user',
    cascade="all, delete, delete-orphan",
    single_parent=True,
    order_by="desc(Note.timestamp)"
  )

class UserSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = User
    load_instance = True
    sqla_session = db.session
    include_relationships = True

  notes = fields.Nested(NoteSchema, many=True)


user_schema = UserSchema()
users_schema = UserSchema(many=True)