from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, DateTimeField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    title = StringField('Title of your pitch', validators=[Required()])
    content = TextAreaField('Content', validators=[Required()])
    # date = DateTimeField('Date')
    category = SelectField('Select a category', choices=[('25', 'Job Pitches'), ('26', 'Movie Pitches'), ('27', 'Product Pitches')])
    submit = SubmitField('Submit')