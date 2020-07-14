from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, DateTimeField
from wtforms.validators import Required, Length

class PitchForm(FlaskForm):

    title = StringField('Title of your pitch', validators=[Required()])
    content = TextAreaField('Content', validators=[Required(), Length(min=6, max=255, message="Username should be more than 6 characters")])
    # date = DateTimeField('Date')
    category = SelectField('Select a category', choices=[('31', 'Job Pitches'), ('27', 'Movie Pitches'), ('26', 'Product Pitches'), ('32', 'Motivation Pitches')])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    content = TextAreaField('Content', validators=[Required()])
    submit = SubmitField('Comment')

class CategoryForm(FlaskForm):
    name = StringField('Name', validators=[Required()])
    submit = SubmitField('Submit')