from flask import Blueprint, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_mail import Mail
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
cors = CORS()
migrate = Migrate()
mail = Mail()
bcrypt = Bcrypt()