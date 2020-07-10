from flask import render_template

from . import main

@main.route('/')
def index():
    title = "hi"

    return render_template('main/index.html', title=title)