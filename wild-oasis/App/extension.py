from flask import (Flask, render_template, redirect, 
                   url_for, abort, Blueprint) 
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required
from flask_restful import Resource





db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
