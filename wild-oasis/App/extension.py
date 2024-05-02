from flask import (Flask, render_template, redirect, 
                   url_for, abort, Blueprint, redirect, request, flash, current_app, session) 
from flask_cors import CORS
from flask_mail import Mail, Message
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required
from flask_restful import Resource
from flask_bcrypt import Bcrypt
from flask_toastr import Toastr
from flask_login import LoginManager, current_user, login_required, logout_user, login_user, UserMixin
from itsdangerous import URLSafeTimedSerializer
import os

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
bcrypt = Bcrypt()
mail = Mail()
serializer = URLSafeTimedSerializer(os.getenv("SECRET_KEY"))
toastr = Toastr()
login_manager = LoginManager()
