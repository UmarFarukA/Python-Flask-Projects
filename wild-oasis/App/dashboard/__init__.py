
def create_dashboard_module(app, **kwargs):
    from App.dashboard.routes import dashboard
    app.register_blueprint(dashboard)