import secrets
import os
from datetime import datetime
from App.extension import request, flash, redirect, url_for, current_app
from werkzeug.utils import secure_filename


def current_date():
    cur_datetime = datetime.now()
    # d = date.day
    # m = date.month
    # y = date.year
    
    cur_date = cur_datetime.date().strftime("%Y-%m-%d")
    return cur_date

def image_name(path, image="default.png"):
    """This function creates and return image name"""
    file = request.files[image]
    filename = secure_filename(file.filename)
    if filename != "":
        random_hex = secrets.token_hex(8)
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in current_app.config["UPLOAD_EXTENSIONS"]:
            flash("File format not allowed", "danger")
            return redirect(url_for(path))
        return random_hex + file_ext

def reset_email(email):
    ...

class ValidationError(Exception):
    """Exception raised for validation errors."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)