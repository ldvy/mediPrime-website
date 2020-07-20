from . import bp
from flask import render_template, redirect, url_for, current_app, session, request


@bp.route('/')
def home_view():
    return render_template('home/index.html')


@bp.route('/<language>')
def change_language(language):
    if language in current_app.config['LANGUAGES']:
        session['lang'] = language
    return redirect(url_for(session['url']))
