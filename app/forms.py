from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class SigninForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign-In')

class PostForm(FlaskForm):
    char_name = StringField('Character', validators=[DataRequired()])
    char_description = StringField('Description', validators=[DataRequired()])
    char_super_powers = StringField('Super Powers', validators=[DataRequired()])
    comics_app_in = StringField('Comics Featured In', validators=[DataRequired()])
    movies_app_in = StringField('Movies Featured In', validators=[DataRequired()])
    submit = SubmitField('Publish')

class UserSearchForm(FlaskForm):
    user = StringField('User', validators=[DataRequired()])
    submit = SubmitField('Search')

class CommissionForm(FlaskForm):
    name = TextAreaField('Name', validators=[DataRequired()])
    email = TextAreaField('Email', validators=[DataRequired()])
    subject = TextAreaField('Subject', validators=[DataRequired()])
    message = TextAreaField('Request', validators=[DataRequired()])
    budget = StringField('Budget', validators=[DataRequired()])
    submit = SubmitField("Send")

class ContactForm(FlaskForm):
    name = TextAreaField("Name")
    email = TextAreaField("Email")
    subject = TextAreaField("Subject")
    message = TextAreaField("Message")
    submit = SubmitField("Send")