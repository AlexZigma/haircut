import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('user', __name__)




@bp.route('/')
# @login_required
def home():
    db = get_db()
    shops = db.execute('SELECT * FROM shop')
    return render_template('user/index.html', shops=shops)

def get_shop(id):
    db = get_db()
    shop = db.execute('SELECT * FROM shop WHERE shop.id = ?', (id, )).fetchone()
    return shop

def get_pricelist(id):
    db = get_db()
    pricelist = db.execute('SELECT * FROM pricelist' 
                           ' WHERE shop_id = ?', (id,)).fetchall()
    return pricelist

@bp.route('/<int:id>/shop')
# @login_required
def shop(id):
    shop = get_shop(id)
    pricelist = get_pricelist(id)
    # print(shop)
    return render_template('user/shop.html', shop=shop, pricelist=pricelist)
