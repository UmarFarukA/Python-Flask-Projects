from App.booking.routes import booking

def create_booking_module(app, **kwargs):
    from App.models.booking import Booking
    app.register_blueprint(booking)