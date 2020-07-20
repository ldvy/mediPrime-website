from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FieldList, BooleanField
from wtforms.fields import MultipleFileField
from wtforms.validators import DataRequired

from flask_babelex import lazy_gettext as _l


# Basic login form
class LoginForm(FlaskForm):
    username = StringField(_l("Username"), validators=[DataRequired()])
    password = PasswordField(_l("Password"), validators=[DataRequired()])
    remember_me = BooleanField(_l('Remember Me'))


# Base form for Reagent view in purpose of handling Json field
class BaseJsonForm(FlaskForm):
    packing = StringField(_l("Packing"), validators=[DataRequired()])
    code = StringField(_l("Code"), validators=[DataRequired()])
