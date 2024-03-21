from App.extensions import (Blueprint, jsonify, abort, request, bcrypt, db, 
                            login_required, current_user, logout_user)
from App.api.models.users import Users


auth = Blueprint("auth", __name__)


@auth.route("/login", methods=['POST'])
def login(data):
    """This routes returns staus of login"""
    try:
        email = data.email
        user = Users.query.filter_by(email == email).first()
        if user is None:
            return jsonify({
                "status": "error",
                "is_authenticated": False,
                "message": "Invalid login details"
            })
        
        if current_user.is_authenticated:
            return jsonify({
                "status": "ok",
                "is_authenticated": True,
                "message": "User already authenticated"
            })
        
        if user:
            if bcrypt.check_password_hash(user.password, data.password):
                return jsonify({
                    "status": "ok",
                    "is_authenticated": True,
                    "message": "Successfully authenticated"
                })
    except:
        abort(400)


@auth.route("/logout")
@login_required
def logout():
    """This route logs out the user"""
    logout_user()
    return jsonify({
        "status": "ok",
        "is_authenticated": False,
        "message": "User successfully logout"
    })

@auth.route("/changePassword")
@login_required
def change_password(data, user_id):
    try:
        user = Users.query.get(user_id)
        if user is None:
            return jsonify({
                "status": "error",
                "message": "Error in changing user password"
            })
        if bcrypt.check_password_hash(user.password, data.old_password):
            if data.new_password != data.confirm_password:
                return jsonify({
                    "status": "error",
                    "message": "Confirm Password do not match"
                })
            user.password = bcrypt.generate_password_hash(data.new_password)
            return jsonify({
                "status": "ok",
                "message": "Password successfully updated"
            })
    except:
        abort(400)
    else:
        ...
