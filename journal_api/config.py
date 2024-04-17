import os
import pathlib
from dotenv import load_dotenv
import connexion
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


load_dotenv()

base_dir = pathlib.Path(__file__).parent.resolve()

connex_app = connexion.App(__name__, specification_dir=base_dir)

app = connex_app.app

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://{}:{}@{}/{}".format(
        os.getenv('DB_USER'), os.getenv('DB_PWD'),
        'localhost:5432', os.getenv('DB_NAME')
    )
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)
ma = Marshmallow(app)