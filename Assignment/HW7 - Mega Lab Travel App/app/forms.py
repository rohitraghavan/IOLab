from flask.ext.wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired


class TripForm(Form):
    '''
    Add trip input form fields
    '''
    name_of_trip = StringField('name_of_trip', validators=[DataRequired()])
    destination = StringField('destination', validators=[DataRequired()])
    friend2 = SelectField('friend2', validators=[DataRequired()])


class SignupForm(Form):
    '''
    Add user input form fields
    '''
    user_name = StringField('user_name', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])


class LoginForm(Form):
    '''
    Login form fields
    '''
    user_name = StringField('user_name', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])

