from App.settings.routes import settings

def create_setting_module(app, **kwargs):
    from App.models.settings import Setting
    app.register_blueprint(settings)