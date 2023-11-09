from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


from cuevana.db import get_db

bp = Blueprint('movies', __name__, url_prefix='/movies/')

@bp.route('/')
def index():
    db = get_db()
    movie = db.execute(
        """SELECT f.title AS nombre, l.name AS lenguaje, release_year as fecha
         FROM film f JOIN language l ON f.language_id = l.language_id 
         ORDER BY f.film_id DESC"""
    ).fetchall()


    return render_template('movies/index.html', movie=movie)

