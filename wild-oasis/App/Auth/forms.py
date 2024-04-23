from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import InputRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    """This class defines the login fields"""
    username = StringField("Username", validators=[
        Email(message="Invalid email address"),
        InputRequired("Username is required")
    ])

    password = PasswordField("Password", validators=[
        InputRequired("Password is required to log in")
    ])

    login = SubmitField("Login")


class SignUpForm(FlaskForm):
    """This form provides field for registering new user"""
    fname = StringField("First Name", validators=[
        InputRequired(message="First Name is required"), 
        Length(min=2, max=25, message="First Name can't be less than 2 and maximum of 25")
    ])
    lname = StringField("Last Name",validators=[
        InputRequired(message="Last Name is required"), 
        Length(min=2, max=25, message="Last Name can't be less than 2 and maximum of 25")
    ])

    email = EmailField("Email Addres", validators=[
        InputRequired(message="Valid email is required")
    ])
    password = PasswordField("Password", validators=[
        InputRequired(message="Password is required"),
        EqualTo("confirm_password", message="Password Must match"),
        Length(min=8, max=16, message="Password must be at least 8 characters long")
    ])
    confirm_password = PasswordField("Confirm Password")

    submit = SubmitField("Sign Up")


class ChangePasswordForm(FlaskForm):
    """This form provides fields for changing User password"""
    current_password = PasswordField("Current Password", validators=[
        InputRequired(message="Password is required"),
        Length(min=8, max=16, message="Password must be at least 8 characters long")
    ])

    new_password = PasswordField("New Password", validators=[
        InputRequired(message="Password is required"),
        EqualTo("confirm_new_password", message="Password Must match"),
        Length(min=8, max=16, message="Password must be at least 8 characters long")
    ])
    confirm_password = PasswordField("confirm_new_password")

    submit = SubmitField("Update")


class ResetPasswordForm(FlaskForm):
    """This class provides fields for resetting password"""
    email = EmailField("Email Address", validators=[
        InputRequired(message="Valid email is required"),
        Email("Kindly provide a valid email address")
    ])
    reset = SubmitField("Reset")