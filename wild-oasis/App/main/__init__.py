
def create_main_module(app, **kwargs):
    from App.main.routes import main
    app.register_blueprint(main)