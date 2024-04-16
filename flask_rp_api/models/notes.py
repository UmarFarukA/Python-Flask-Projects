from datetime import datetime
from config import db, ma

class Note(db.Model):
  __tablename__ = "note"
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
  content = db.Column(db.String, nullable=False)
  timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class NoteSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Note
    load_instance = True
    sqla_session = db.session
    # include_fk = True


note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)