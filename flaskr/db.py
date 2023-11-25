import sqlite3
import json

import click
from flask import current_app, g




def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
        
def add_data():
    db = get_db()
    with open('flaskr/data.json', encoding='utf-8') as f:
        data = json.load(f)
    
    for d in data:
        values = (d['title'], d['icon'], d['place'], d['short_discription'])
        db.execute('INSERT INTO shop (shopname, icon, location, description)'
                   'VALUES (?, ?, ?, ?)', values)
        db.commit()


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

@click.command('add-data')
def add_data_command():
    add_data()
    click.echo('Data has been added')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(add_data_command)
    
