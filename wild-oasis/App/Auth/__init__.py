
from App.extension import login_manager

login_manager.login_view = "Auth.login"
login_manager.session_protection = "strong"
login_manager.login_message = "Please login to access this page"
login_manager.login_message_category = "info"

def load_user(userId):
    from App.models.users import User
    return User.query.get(userId)

def create_auth_module(app, **kwargs):
    from App.Auth.routes import auth
    app.register_blueprint(auth)