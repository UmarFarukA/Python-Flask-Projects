from App.extensions import Blueprint, jsonify, abort, request, bcrypt, db, login_required, current_user
from App.api.models.users import Users, users_schema, user_schema

users = Blueprint('users', __name__, url_prefix="api/vi")


@users.route('/users', methods=['GET'])
def get_users():
    """This route returns all users"""
    try:
        all_users = Users.query.all()
        return jsonify({
            "status": "ok",
            'message': 'success',
            "count": len(all_users),
            "data": users_schema.dump(all_users)
        })
    except:
        abort(400)

@users.route('/users/<int:user_id', methods=['GET'])
def get_user(user_id):
    """This routes returns user with the specified ID
        Parameters:
            user_id (Integer): The id of the user
    """
    try:
        user = Users.query.filter_by(id == user_id).first()
        return jsonify({
            "status": "ok",
            'message': 'success',
            "data": user_schema.dump(user)
        })
    except:

        abort(404)

@users.route('/create_user', methods=['POST'])
def create(user):
    """This routes create new user"""
    try:
        email = user.get("email")
        password = user.get("password")
        name = user.get("name")
        mname = user.get("mname")
        lname = user.get("lname")

        harsh_password = bcrypt.generate_password_hash(password)

        newUser = Users(name, mname, lname, email, harsh_password)

        email_status = newUser.validate_email(email)

        if email_status is not None:
            return jsonify({
                "status": "Error creating new user",
                'message': 'User all exists',
            })

        if email_status is None:
            newUser.insert()
            return jsonify({
                "status": "ok",
                'message': 'success',
            })
        
    except:
        abort(401)


@users.route('/update_user/<int:user_id>', methods=['PATCH'])
def update_user(data, user_id):
    """This route update users details"""
    try:
        user = Users.query.filter_by(id == user_id).first()

        if user is None:
            return jsonify({
                "status": "Error",
                "message": "User not found"
            })
        
        user.name = data.name
        if user.mname:
            user.mname = data.mname
        user.lname = data.lname

        db.session.commit()

        return jsonify({
            "status": "ok",
            "message": "record successfully updated",
        })

    except:
        abort(404)