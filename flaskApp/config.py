import os
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    WTF_CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}/{}".format(os.getenv("DB_USER"), os.getenv("DB_PWD"),\
                                                                'localhost:5432', os.getenv("DB_NAME"))\
                                                                or 'sqlite:///' + os.path.join(basedir, 'app.db'
                                                                )
    SQLALCHEMY_TRACK_MODIFICATIONS = False