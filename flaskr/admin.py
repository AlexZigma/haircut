import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/')
# @login_required
def home():
    db = get_db()
    shops = db.execute('SELECT * FROM shop')
    return render_template('admin/index.html', shops=shops)

def get_shop(id):
    db = get_db()
    shop = db.execute('SELECT * FROM shop WHERE shop.id = ?', (id, )).fetchone()
    return shop

def get_pricelist(id):
    db = get_db()
    pricelist = db.execute('SELECT * FROM pricelist' 
                           ' WHERE shop_id = ?', (id,)).fetchall()
    return pricelist

@bp.route('/create', methods=('GET', 'POST'))
# @login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
# @login_required
def update(id):
    shop = get_shop(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('admin/update.html', shop=shop)

@bp.route('/<int:id>/delete', methods=('POST',))
# @login_required
def delete(id):
    get_shop(id)
    db = get_db()
    db.execute('DELETE FROM shop WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('admin.home'))
