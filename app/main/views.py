from flask import render_template, redirect, url_for, abort, request
from .forms import PitchForm
from ..auth.forms import UpdateForm
from . import main
from .. import photos, db
from ..models import Pitch, Category, User
from flask_login import login_required, current_user

@main.route('/', methods=['GET', 'POST'])
def index():
    title = "Pitch"
    pitches = Pitch.get_pitches()
    return render_template('main/index.html', title=title, pitches=pitches)

@main.route('/add', methods= ['GET', 'POST'])
@login_required
def add_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        category = form.category.data
        # date = form.date.data
        # cat_int = int(category)
        # print(type(content))
        pitch = Pitch(title=title, content=content, category_id=category, user=current_user)
        pitch.save_pitch()
        return redirect(url_for('main.index'))
    return render_template('main/create_pitch.html', pitch_form=form)
    

# @main.route('/other')
# def other_index():
#     word = 'here'
#     return render_template('main/index.html', title=word)

# @main.route('/pitch')
# def display_pitch():
#     pitch = Pitch.get_pitches()
#     print(pitch[1].category.name)
#     return render_template('main/pitch.html', pitch=pitch)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(name = uname).first()

    if user is None:
        abort(404)
    return render_template('profile/profile.html', user=user)

@main.route('/user/<uname>/update', methods= ['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(name=uname).first()
    update_form = UpdateForm()
    if user is None:
        abort(404)

    if update_form.validate_on_submit():
        user.bio = update_form.bio.data
        User.update_user(user)
        return redirect(url_for('.profile', uname=user.name))
    return render_template('profile/update.html', update_form = update_form)

@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(name = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))

@main.route('/upvote/<int:pitch_id>')
@login_required
def upvote(pitch_id):
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    if pitch.upvotes is None:
        pitch.upvotes = 0
        pitch.upvotes += 1
    else:
        pitch.upvotes += 1
    db.session.commit()
    return redirect(url_for('main.index'))
    
    
@main.route('/downvote/<int:pitch_id>')
@login_required
def downvote(pitch_id):
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    if pitch.downvotes is None:
        pitch.downvotes = 0
        pitch.downvotes += 1
    else:
        pitch.downvotes += 1
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/comment/<int:pitch_id>')
@login_required
def comment_quotes(pitch_id):
    pass
    


