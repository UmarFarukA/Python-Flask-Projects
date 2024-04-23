from wtforms import EmailField, StringField, DateField, PasswordField, SubmitField
from wtforms.validators import InputRequired, EqualTo, Length
from flask_wtf import FlaskForm

class RegisterForm(FlaskForm):
    fname = StringField("First Name", 
                        validators=[InputRequired(message="First Name is required"), 
                                    Length(min=2, max=25, 
                                           message="First Name can't be less than 2 and maximum of 25")])
    lname = StringField("Last Name", 
                        validators=[InputRequired(message="Last Name is required"), 
                                    Length(min=2, max=25, 
                                           message="Last Name can't be less than 2 and maximum of 25")])
    email = EmailField("Email Addres", validators=[InputRequired(message="Valid email is required")])
    password = PasswordField("Password", InputRequired(message="Password is required"),
                             EqualTo("confirm_password", message="Password Must match"),
                             Length(min=8, max=16, message="Password must be at least 8 characters long"))
    confirm_password = PasswordField("Confirm Password")

    submit = SubmitField("Register")

