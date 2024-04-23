import os
import pathlib
from dotenv import load_dotenv

load_dotenv()

class Config:
    base_dir = pathlib.Path(__file__).parent.resolve()
    WTF_CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}/{}".format(
        os.getenv('DB_USER'), os.getenv('DB_PWD'),
        'localhost:5432', os.getenv('DB_NAME')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif']
    UPLOAD_PATH = 'static/images/uploads'
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv("MAIL_PORT")
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")


class DevConfig(Config):
    ...

class ProdConfig(Config):
    ...