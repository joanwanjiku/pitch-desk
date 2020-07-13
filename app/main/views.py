from flask import render_template, redirect, url_for
from .forms import PitchForm
from . import main
from ..models import Pitch, Category

@main.route('/', methods=['GET', 'POST'])
def index():
    title = "hi"
    form = PitchForm()
    pitches = Pitch.get_pitches()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        category = form.category.data
        # date = form.date.data
        # cat_int = int(category)
        # print(type(content))
        pitch = Pitch(title=title, content=content, category_id=category)
        pitch.save_pitch()
        return redirect(url_for('main.display_pitch'))
    return render_template('main/index.html', title=title, pitch_form=form, pitches=pitches)

@main.route('/other')
def other_index():
    word = 'here'
    return render_template('main/index.html', title=word)

@main.route('/pitch')
def display_pitch():
    pitch = Pitch.get_pitches()
    print(pitch[1].category.name)
    return render_template('main/pitch.html', pitch=pitch)