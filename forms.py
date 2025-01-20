from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class RegisterForm(FlaskForm):
    username = StringField("Enter your username", validators=[DataRequired(), Length(min=6, max=16)])
    password = PasswordField("Enter your password", validators=[DataRequired(), Length(min=8, max=16)])
    repeat_password = PasswordField("Repeat your password", validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    mail = StringField("Enter your mail", validators=[DataRequired(), Email()])
    phone_number = StringField("Enter your phone number", validators=[DataRequired()])
    submit = SubmitField("Register")

class FeedbackForm(FlaskForm):
    username = StringField("Enter your username", validators=[DataRequired(), Length(min=6, max=16)])
    feedback = TextAreaField("Enter your feedback", validators=[DataRequired()])
    submit = SubmitField("Submit Feedback")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")