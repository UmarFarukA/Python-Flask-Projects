from datetime import datetime
from config import db, ma

class Note(db.model):
    __tablename__ = "note"
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"))
    content = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(150), unique=True)
    fname = db.Column(db.String(150))
    timestamp =db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    notes = db.relationship(Note, backref="person", cascade="all, delete, delete-orphan",
            single_parent=True, order_by="desc(Note.timestamp)")


class PeopleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = People
        load_instance = True
        sqla_session = db.session


person_schema = PeopleSchema()
people_schema = PeopleSchema(many=True)
