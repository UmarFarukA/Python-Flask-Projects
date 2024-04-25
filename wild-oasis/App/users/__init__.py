from App.users.route import users

def create_users_module(app, **kwargs):
   from App.models.users import User
   app.register_blueprint(users)