import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('company', __name__)

active = 0

@bp.route('/home')
@login_required
def home():
    active = 0
    return render_template('user/home.html', active=active)

@bp.route('/profile')
@login_required
def profile():
    active = 1
    return render_template('user/profile.html', active=active)

@bp.route('/workers')
@login_required
def workers():
    active = 2
    return render_template('user/workers.html', active=active)

@bp.route('/service')
@login_required
def service():
    active = 3
    return render_template('user/service.html', active=active)

@bp.route('/stats')
@login_required
def stats():
    active = 4
    return render_template('user/stats.html', active=active)



# @bp.route('/<int:id>')
# @login_required
# def user_page(id):
#     return str(id)
#     return render_template('user.html', id=id)