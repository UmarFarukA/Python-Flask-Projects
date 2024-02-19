from flask import Flask
from config import Config
from app.extension import db, migrate

def create_app(config_class=Config):
    
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initializing flask extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Registering blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.posts import bp as posts_bp
    app.register_blueprint(posts_bp, url_prefix='/posts')

    from app.questions import bp as questions_bp
    app.register_blueprint(questions_bp, url_prefix='/questions')


    @app.route('/test')
    def test():
        return "<h1>Testing the flask application factory </h1>"
    
    return app