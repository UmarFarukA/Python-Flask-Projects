from App.extension import Blueprint, render_template

booking = Blueprint("booking", __name__)


@booking.route("/bookings", methods=["GET", "POST"])
def index():
    return render_template("booking/index.html")