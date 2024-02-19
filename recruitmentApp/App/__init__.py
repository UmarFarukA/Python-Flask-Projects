from flask import Flask
from App.extensions import cors, migrate, mail, bcrypt, db
import config

app = Flask(__name__)

def create_app(config=config):

    cors.init_app(app)
    migrate.init_app(app)
    mail.init_app(app)
    bcrypt.init_app(app)

    return app