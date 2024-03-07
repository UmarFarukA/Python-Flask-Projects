from flask import Blueprint, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from wtforms.validators import ValidationError
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_required, current_user, logout_user

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
mail = Mail()
bcrypt = Bcrypt()
ma = Marshmallow()
login_manager = LoginManager()