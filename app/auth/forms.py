from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField, TextAreaField
from wtforms.validators import Required, EqualTo, Length, Email
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Enter your email', [ Required(), Email() ])
    username = StringField('Username', validators=[Required(), Length(min=6, max=20, message="Username should be more than 6 characters")])
    password = PasswordField('Enter password', validators=[Required(), EqualTo('confirm_password', message='Passwords should match'), Length(min=6, max=20, message="Password should be between 6 and 20 characters")])
    confirm_password = PasswordField('Repeat password', validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('There is an account with that email')
    
    def validate_username(self, data_field):
        if User.query.filter_by(name=data_field.data).first():
            raise ValidationError('Username is taken')
        
class LoginForm(FlaskForm):
    email = StringField('Your email address',[ Required(), Email() ])
    password = PasswordField('Your password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class UpdateForm(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Update')
