from App.extension import Blueprint, render_template

users = Blueprint("users", __name__)

@users.route("/users", methods=["GET", "POST"])
def index():
    return render_template("users/index.html")