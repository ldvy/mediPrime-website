from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FieldList, BooleanField
from wtforms.validators import DataRequired


# Basic login form
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')


# Base form for Reagent view in purpose of handling Json field
class BaseJsonForm(FlaskForm):
    packing = StringField("Packing", validators=[DataRequired()])
    code = StringField("Code", validators=[DataRequired()])
