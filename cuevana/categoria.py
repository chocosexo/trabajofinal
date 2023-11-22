from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
#from flaskr.auth import login_required
from cuevana.db import get_db

bp = Blueprint('categoria', __name__)
bp = Blueprint('categoria', __name__, url_prefix="/categoria")

@bp.route('/')
def index():
    db = get_db()
    categoria = db.execute(
        """SELECT name
            FROM category
            ORDER BY name ASC """
    ).fetchall()
    return render_template('categoria/index.html', categoria=categoria)
def get_categoria(id):
    categoria = get_db().execute(
        """SELECT *
            FROM category
            WHERE category_id = ? """,
            (id,)
    ).fetchone()
    if categoria is None:
        abort(404, f"Post id {id} doesn't exist.")
@bp.route('/<int:id>/detalle', methods=['GET'])
def mostrarcategoria(id):
    category = get_categoria(id)
    return render_template('categoria/index.html', categoria=category)