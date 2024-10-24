from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo
from models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    is_marketer = BooleanField('Are you a digital marketer?')
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class SkillForm(FlaskForm):
    title = StringField('Skill Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Add Skill')

class RatingForm(FlaskForm):
    score = StringField('Rating (1-5)', validators=[DataRequired()])
    comment = TextAreaField('Comment')
    submit = SubmitField('Submit Rating')

class ForgotPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Send Reset Link')
