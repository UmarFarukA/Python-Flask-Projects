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
                "message": "Invalid login details"
            })
        
        if current_user.is_authenticated:
            return jsonify({
                "status": "ok",
                "authenticated": True,
                "message": "User already authenticated"
            })
        
        if user:
            if bcrypt.check_password_hash(user.password, data.password):
                return jsonify({
                    "status": "ok",
                    "authenticated": True,
                    "message": "Successfully authenticated"
                })
    except:
        abort(400)


@auth.route("/logout")
@login_required
def logout():
    """This route logout the user"""
    logout_user()
    return jsonify({
        "status": True,
        "message": "User successfully logout"
    })