from App.guests.routes import guest

def create_guest_module(app, **kwargs):
    from App.models.guest import Guest
    app.register_blueprint(guest)