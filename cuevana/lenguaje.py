from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


from cuevana.db import get_db

bp = Blueprint('lenguaje', __name__)

@bp.route('/lenguaje')
def index():
    db = get_db()
    lenguaje = db.execute(
        'SELECT *'
        ' FROM language '
        ' ORDER BY name '
    ).fetchall()


    return render_template('lenguaje/index.html', lenguaje=lenguaje)