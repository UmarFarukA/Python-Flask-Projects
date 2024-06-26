import config
from App.extension import (Flask, db, migrate, cors, mail, toastr, login_manager)



def create_app(config=config.Config):
    app = Flask(__name__)
    app.config.from_object(config) 
    

    # Initializing extensions install with the app instance
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    toastr.init_app(app)
    

    # imported blueprint modules
    from App.main import create_main_module as main_module
    from App.Auth import create_auth_module as auth_module
    from App.cabin import create_cabin_module as cabin_module
    from App.booking import create_booking_module as booking_module
    from App.guests import create_guest_module as guest_module
    from App.settings import create_setting_module as setting_module
    from App.users import create_users_module as users_module
    from App.dashboard import create_dashboard_module as dashboard_module


    # invoking the modules
    main_module(app)
    auth_module(app)
    cabin_module(app)
    booking_module(app)
    guest_module(app)
    setting_module(app)
    users_module(app)
    dashboard_module(app)


    return app