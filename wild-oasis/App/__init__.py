import config
from App.extension import Flask, db, migrate, cors, login_manager, mail, serializer




def create_app(config=config.Config):
    app = Flask(__name__)
    app.config.from_object(config)
    

    # Initializing extensions install with the app instance
    db.init_app(app)
    migrate.init_app(app)
    cors.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    


    # imported blueprint modules
    from App.Auth import create_auth_module as auth_module
    from App.cabin import create_cabin_module as cabin_module


    # invoking the modules
    auth_module(app)
    cabin_module(app)


    return app