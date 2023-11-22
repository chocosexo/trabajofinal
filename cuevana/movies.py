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

@bp.route('/<int:id>/detalle', methods=['GET'])
def mostrarPeliculas(id):
    categoria = get_db().execute(
        """SELECT title as titulo, count(fc.film_id) as peliculas
            FROM film f JOIN film_category fc USING (film_id)
            GROUP BY f.film_id
            WHERE f.film_id = ? """,
            (id,)
    ).fetchone()

    pelis = get_db().execute(
        """SELECT title
            FROM category
            WHERE category_id = ? """,
            (id,)
    ).fetchall()

    return render_template('movies/index.html', movie=movie)

