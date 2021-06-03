from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, Booleanfield
from wtforms.validators import DataRequired, EqualTo, Email

class UserInfoForm(FlaskForm):
    #username = StringField('Username', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    #email = StringField('Email', validators=[DataRequired(), Email()])
    number = StringField('Phone Number', validators=[DataRequired()])
    #password = PasswordField('Password', validators=[DataRequired()])
    #confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField()



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField()
    