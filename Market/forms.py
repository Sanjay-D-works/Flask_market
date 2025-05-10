from click import password_option
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class RegisterFrom(FlaskForm):
    username = StringField(label='username')
    email_address = StringField(label='email')
    password1 = PasswordField(label='password')
    password2 = PasswordField(label='password')
    submit = SubmitField(label='submit')