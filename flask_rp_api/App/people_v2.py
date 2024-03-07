from flask import abort, make_response
from config import db
from models import People, people_schema, person_schema



def read_all():
    people = People.query.all()
    print(people)
    return people_schema.dump(people)

def create(person):
    lname = person.get("lname")
    existing_person = People.query.filter(People.lname == lname).one_or_none()

    if existing_person is None:
        new_person = person_schema.load(person, session=db.session)
        db.session.add(new_person)
        db.session.commit()
        return person_schema.dump(new_person), 201
    else:
        abort(
                406,
                f"Person with last name {lname} alread exists",
        )

def read_one(lname):
    person = People.query.filter(People.lname == lname).one_or_none()

    if person:
        return person_schema.dump(person)
    else:
        abort(
                404, f"Person with last name {lname} not found"
        )

def update(lname, person):
    existing_person = People.query.filter(People.lname == lname).one_or_none()


    if existing_person:
        update_person = people_schema.load(person, session=db.session)
        existing_person.fname = update_person.fname
        db.session.merge(existing_person)
        db.session.commit()
        return person_schema.dump(existing_person), 201
    else:
        abort(
                404, f"Person with last name {lname} not found"
        )

def delete(lname):
    existing_person = People.query.filter(People.lname == lname).one_or_none()

    if existing_person:
        db.session.delete(existing_person)
        db.session.commit()
        return make_response(f"{lname} successfully deleted", 200)
    else:
        abort(
                404,
                f"Person with last name {lname} not found"
        )