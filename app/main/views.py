from flask import render_template, redirect, url_for, abort, request
from .forms import PitchForm, CommentForm, CategoryForm
from ..auth.forms import UpdateForm
from . import main
from .. import photos, db
from ..models import Pitch, Category, User, Comment
from flask_login import login_required, current_user

@main.route('/', methods=['GET', 'POST'])
def index():
    title = "Pitch"
    movie_pitches = Pitch.get_pitches(1)
    product_pitches = Pitch.get_pitches(2)
    job_pitches = Pitch.get_pitches(3)
    motivation_pitches = Pitch.get_pitches(4)
    return render_template('main/index.html', title=title, movie_pitches=movie_pitches, product_pitches=product_pitches, job_pitches=job_pitches, motivation_pitches=motivation_pitches )

@main.route('/addcat', methods=['POST', 'GET'])
@login_required
def add_cat():
    form = CategoryForm()
    if form.validate_on_submit():
        name = form.name.data
        cat = Category(name=name)
        cat.save_category()
        return redirect(url_for('main.add_pitch'))
    return render_template('main/create_cat.html', form=form)

@main.route('/add', methods= ['GET', 'POST'])
@login_required
def add_pitch():
    form = PitchForm()
    categories = Category.get_all_cats()

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        cate = request.form['category']
        pitch = Pitch(title=title, content=content, category_id=cate, user=current_user)
        pitch.save_pitch()
        return redirect(url_for('main.index'))
    return render_template('main/create_pitch.html', pitch_form=form, categories=categories)

    # if form.validate_on_submit():
    #     title = form.title.data
    #     content = form.content.data
    #     category = form.category.data
    #     pitch = Pitch(title=title, content=content, category_id=category, user=current_user)
    #     pitch.save_pitch()
    #     return redirect(url_for('main.index'))
    # return render_template('main/create_pitch.html', pitch_form=form, categories=categories)


@main.route('/pitch/<int:pitch_id>')
def display_pitch(pitch_id):
    pitch = Pitch.get_pitch_by_id(pitch_id)
    comments= Comment.get_all_comments(pitch_id)
    return render_template('main/pitch.html', pitch=pitch, comments=comments)

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

@main.route('/pitch//comment/new/<int:pitch_id>', methods=['GET', 'POST'])
@login_required
def comment_pitch(pitch_id):
    comment_form = CommentForm()
    pitch= Pitch.get_pitch_by_id(pitch_id)
    if comment_form.validate_on_submit():
        content = comment_form.content.data
        new_comment = Comment(content=content, pitch_id=pitch_id)
        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('main.display_pitch', pitch_id=pitch_id))
    return render_template('main/pitch_comment.html', form = comment_form, pitch=pitch)

