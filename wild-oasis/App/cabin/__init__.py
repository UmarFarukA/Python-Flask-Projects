
def create_cabin_module(app, **kwargs):
    from App.cabin.routes import cabin
    app.register_blueprint(cabin)