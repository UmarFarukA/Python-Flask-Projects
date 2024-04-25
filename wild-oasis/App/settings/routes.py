from App.extension import Blueprint, render_template

settings = Blueprint("settings", __name__)


@settings.route("/settings", methods=["GET", "POST"])
def index():
    return render_template("settings/index.html")