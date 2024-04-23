from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import InputRequired


class AddCabinForm(FlaskForm):
    """
        This class creates fields for creating New Cabin
    """
    name = StringField("Cabin Name", validators=[InputRequired(message="Cabin Name is required")])
    maxCapacity = IntegerField("Maximum Capacity", validators=[
        InputRequired("Max number for the cabin is required")
    ])
    price = FloatField("Price", validators=[
        InputRequired("Cabin Price is required")
    ])
    discount = IntegerField("Discount", validators=[InputRequired("Cabin discount is required")])

    image = StringField("Image")

    add = SubmitField("Add Cabin")


class EditCabinForm(FlaskForm):
    """This class provides fields for updating existing cabin"""
    name = StringField("Cabin Name", validators=[InputRequired(message="Cabin Name is required")])
    maxCapacity = IntegerField("Maximum Capacity", validators=[
        InputRequired("Max number for the cabin is required")
    ])
    price = FloatField("Price", validators=[
        InputRequired("Cabin Price is required")
    ])
    discount = IntegerField("Discount", validators=[InputRequired("Cabin discount is required")])

    update = SubmitField("Update Cabin")