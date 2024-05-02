
from App.extension import login_manager



login_manager.login_view = "auth.index"
login_manager.session_protection = "strong"
login_manager.login_message = "Please login to access this page"
login_manager.login_message_category = "info"


@login_manager.user_loader
def load_user(userid):
    from App.models.users import User
    return User.query.get(userid)

def create_auth_module(app, **kwargs):
    
    from App.Auth.routes import auth
    app.register_blueprint(auth)