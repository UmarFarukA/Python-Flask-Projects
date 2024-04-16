from App.Auth.routes import auth

def create_auth_module(app, **kwargs):
    app.register_blueprint(auth)