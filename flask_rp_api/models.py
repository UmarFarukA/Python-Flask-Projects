from datetime import datetime
from config import db, ma


class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    lname = db.Colum(db.String(150), unique=True)
    fname = db.Column(db.String(150))
    timestamp =db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class PeopleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = People
        load_instance = True
        sqla_session = db.session


people_schema = PeopleSchema()
person_schema = PeopleSchema(many=True)