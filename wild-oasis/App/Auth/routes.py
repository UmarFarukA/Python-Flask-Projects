import os
from werkzeug.security import generate_password_hash

from App.extension import (Blueprint, render_template, request, 
                           redirect, url_for, flash, current_app, current_user, 
                           current_user, login_required, db, session, logout_user,
                           mail, Message, serializer)
from App.Auth.forms import LoginForm, SignUpForm, ChangePasswordForm, ResetPasswordForm
from App.models.users import User
from utils import image_name

auth = Blueprint('auth', __name__)

@auth.route("/", methods=['GET'])
@auth.route("/login", methods=["GET", "POST"])
def login():

    """This route authenticate user & redirect to dashboard"""

    login_form = LoginForm(request.form)

    if request.method == "POST" and login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        user = User.query.filter_by(email = username).first()

        if not user:
            flash("danger", f"No user exists with - {username}")
        
        elif user.check_password(password):
            flash("success", "Successfully login")
            return redirect(url_for("users.dashboard"))
        
        else:
            flash("danger", "Invalid password")

    return render_template("Auth/login.html", form = login_form)

@auth.route("/signup", methods=["GET", "POST"])
def sigup():
    """This route register a new user"""
    signup_form = SignUpForm(request.form)

    if request.method == "POST" and signup_form.validate_on_submit():
        email = signup_form.email.data
        fname = signup_form.fname.data
        lname = signup_form.lname.data
        password = signup_form.password.data
        image = "default.png"

        if "image" in request.files:
            image = image_name("image", path="users.index")
        
        # checking for existing user
        existing_user = User.query.filter_by(email = email).first()

        if existing_user:
            flash("danger", "Email address is already in use")
            return redirect(url_for("Auth.signup"))
        
        # creating new user
        new_user = User(email=email, fname=fname, lname=lname, image=image, password=password)
        new_user.insert()
        flash("success", "New User created successfully")
        return redirect(url_for("users.index"))

    return render_template("Auth/signup.htm", form = signup_form)

@auth.route("/reset", methods=["GET", "POST"])
def reset_password():
    """This route reset the user's password"""
    reset_form = ResetPasswordForm(request.form)

    if request.method == "POST" and reset_form.validate_on_submit():
        email = reset_form.email.data

        email_exists = User.query.filter_by(email = email).first()

        if not email_exists:
            flash(f"No user exists with {email}", "red")
            return redirect(url_for("Auth.reset_password"))
        
        token = serializer.dumps(email, salt=os.getenv("SECRET_KEY"))

        reset_link = url_for('reset_password_confirm', token=token, _external=True)

        message = Message(
            subject="Password Reset",
            recipients=[email],
            body=reset_link
        )

        mail.send(message)

        flash("Password reset link has been sent to your mail", "green")
        return redirect(url_for("Auth.login"))

    return render_template("Auth/reset_password.html", form = reset_form)



@auth.route("/reset_password_confirm/<token>", methods=["GET", "POST"])
def reset_password_confirm(token):
    try:
        email = serializer.loads(token, salt=os.getenv("SECRET_KEY"), max_age=3600)
    except:
        flash("The password reset link is invalid or has expired.", "red")
        return redirect(url_for("reset_password"))

    if request.method == "POST":
        user = User.query.filter_by(email = email).first()
        if not user:
            flash(f"No user exists with this mail - {email}.", "red")
            return redirect(url_for("signup"))
        new_password = request.form["password"]
        user.password = generate_password_hash(new_password)
        db.session.commit()
        flash("Password successfully reset.", "green")
        return redirect(url_for("Auth.login"))

    return render_template("reset_password_confirm.html")   


@auth.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    """This route provides functionality for changing password"""
    change_form = ChangePasswordForm(request.form)

    if request.method == "POST" and change_form.validate_on_submit():
        current_password = change_form.current_password.data
        new_password = change_form.new_password.data
        
        if User.check_password(current_password):
            User.set_password(new_password)
            db.session.commit()
            flash("Password successfully changed", "green")
            return redirect(url_for("dashboard.html"))
        else:
            flash("Current password is not valid", "red")
            return redirect(url_for("Auth.change_password"))
    
    return render_template("update_password.html", form = change_form)

@auth.route("/logout")
@login_required
def logout():
    """This function logs the user out of the session"""
    logout_user()
    session.clear()
    flash("You have been logged out successfully", "green")
    return redirect(url_for("login"))
