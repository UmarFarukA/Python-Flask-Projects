from App.extension import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("Auth/login.html")

@auth.route("/sigup", methods=["GET", "POST"])
def sigup():
    ...

@auth.route("/reset", methods=["GET", "POST"])
def reset():
    ...

@auth.route("/change_password", methods=["GET", "POST"])
def change_password():
    ...

@auth.route("/logout", methods=["GET", "POST"])
def logout():
    ...
