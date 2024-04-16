from datetime import datetime
from flask import abort, make_response, request
from config import db
from models.users import User, user_schema, users_schema
from models.notes import Note


def read_all():
    # users = User.query.all()
    users = User.query.join(Note, User.id == Note.user_id).all()
    return users_schema.dump(users)


def create():
    user = request.json
    lname = user.get("lname")
    existing_user = User.query.filter_by(lname=lname).one_or_none()

    if existing_user:
        abort(
            406,
            f"Person with {lname} already exists"
        )
    else:
        new_user = user_schema.load(user, session=db.session)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201

       

def read_one(lname):

    user = User.query.filter_by(lname=lname).one_or_none()

    if user is not None:
        return user_schema.dump(user)
    else:
        abort(
            400,
            f"Person with {lname} not found"
        )

def update(lname):
    user = request.json
    lname = user.get("lname")
    existing_user = User.query.filter_by(lname=lname).one_or_none()

    if existing_user is None:
        abort(
            404,
            f"Person with last name, {lname}, not found"
        )
    else:
        update_user = user_schema.load(user, session=db.session)
        existing_user.fname = update_user.fname
        db.session.merge(existing_user)
        db.session.commit()
        return user_schema.dump(existing_user), 201

def delete(lname):
    existing_user = User.query.filter_by(lname=lname).one_or_none()
    if existing_user:
        db.session.delete(existing_user)
        db.session.commit()
        return make_response(f"{lname} successfully deleted", 200)
    else:
        abort(404, f"Person with {lname} not found")
