from flask import Flask
import config
from App.extensions import (db, migrate, cors, bcrypt, mail, login_manager, ma)


login_manager.login_view = "login"

def create_app(config=config.config):
    """A factory functions for creating app"""

    app = Flask(__name__)

    app.config.from_object(config)

    # Initializing extensions with the app
    bcrypt.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})
    login_manager.init_app(app)
    ma.init_app(app)

    # Importing created blueprints
    from App.api.v1.routes.users import users


    # Registering blueprints
    app.register_blueprint(users)

    return app

