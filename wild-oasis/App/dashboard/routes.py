from App.extension import Blueprint, render_template, login_required

dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/dashboard", methods=["GET", "POST"])
@login_required
def index():
    return render_template("dashboard/index.html")