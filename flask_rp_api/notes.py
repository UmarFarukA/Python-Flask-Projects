# from flask import abort, make_response, request

# from config import db
# from models.notes import Note, note_schema, notes_schema
# from models.users import User


# def create():
#   note_user = request.json
#   try:
#     user_id = note_user.get("user_id")
#     user = User.query.get(user_id)
#     if user:
#       new_note = note_schema.load(note_user, session=db.session)
#       user.notes.append(new_note)
#       db.session.commit()
#       return note_schema.dump(new_note), 201
#     else:
#       abort(
#         404,
#         f"No user exists with the id {user_id}"
#       )
#   except:
#     abort(
#         400,
#         f"Error in creating New Note"
#       )

# def read():
#   notes = Note.query.all()
#   return notes_schema.dump(notes)

# def read_one(note_id):
#   try:
#     if note_id:
#       note = Note.query.filter_by(id=note_id).one_or_none()
#       return note_schema.dump(note)
#     else:
#       abort(
#         404,
#         f"Note with id - {note_id} not found"
#       )
#   except:
#      abort(
#        "Error in fetching Note"
#       )

# def update(note_id):
#   note = request.json
  
#   try:
#     if note_id:
#       existing_note = Note.query.filter_by(id = note_id).one_or_none()
#       if existing_note:
#         existing_note.content = note.get("content")
#         db.session.merge(existing_note)
#         db.session.commit()
#         return note_schema.dump(existing_note)
#       else:
#         abort(
#           400,
#           f"No note exists with the ID of {note_id}"
#         )
#     else:
#       abort(
#         404,
#         f"Note with id - {note_id} not found"
#       )
#   except:
#      abort(
#        "Error in Updating Note"
#       )

# def delete(note_id):
#   try:
#     if note_id:
#       delete_note = Note.query.filter_by(id = note_id).first()
#       if delete_note:
#         db.session.delete(delete_note)
#         db.session.commit()
#         return make_response(f"{note_id} successfully deleted", 204)
#       else:
#         abort(
#           404,
#           f"No note exists with the ID of {note_id}"
#         )
#     else:
#       abort(
#           400,
#           f"Invalid note id"
#         )
#   except:
#     abort(
#       "Error in deleting Note"
#     )

from flask import abort, make_response, jsonify, request
from sqlalchemy.exc import SQLAlchemyError

from config import db
from models.notes import Note, note_schema, notes_schema
from models.users import User

def create():
    try:
        note_data = request.json
        user_id = note_data.get("user_id")
        user = User.query.get(user_id)
        if not user:
            abort(404, f"No user exists with the id {user_id}")
        
        new_note = Note(content=note_data.get("content"), user_id=user_id)
        db.session.add(new_note)
        db.session.commit()
        
        return note_schema.dump(new_note), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        abort(400, f"Error in creating new note: {str(e)}")

def read():
    try:
        notes = Note.query.all()
        print(notes)
        return notes_schema.dump(notes)
    except SQLAlchemyError as e:
        abort(500, f"Error in fetching notes: {str(e)}")

def read_one(note_id):
    try:
        note = Note.query.get(note_id)
        if not note:
            abort(404, f"No note found with id {note_id}")
        return note_schema.dump(note)
    except SQLAlchemyError as e:
        abort(500, f"Error in fetching note: {str(e)}")

def update(note_id):
    try:
        note_data = request.json
        note = Note.query.get(note_id)
        if not note:
            abort(404, f"No note found with id {note_id}")
        
        note.content = note_data.get("content", note.content)
        db.session.commit()
        
        return note_schema.dump(note)
    except SQLAlchemyError as e:
        db.session.rollback()
        abort(400, f"Error in updating note: {str(e)}")

def delete(note_id):
    try:
        note = Note.query.get(note_id)
        if not note:
            abort(404, f"No note found with id {note_id}")
        
        db.session.delete(note)
        db.session.commit()
        
        return make_response(f"Note {note_id} successfully deleted", 204)
    except SQLAlchemyError as e:
        db.session.rollback()
        abort(500, f"Error in deleting note: {str(e)}")
