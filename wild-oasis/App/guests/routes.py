from App.extension import Blueprint, render_template

guest = Blueprint("guest", __name__)

@guest.route("/guest", methods=["GET", "POST"])
def index():
    return render_template("guests/index.html")