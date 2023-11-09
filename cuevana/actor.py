from flask import (
    Blueprint, flash, g, jsonify, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort

from cuevana.db import get_db

bp = Blueprint('actor', __name__, url_prefix='/actor/')
bpapi = Blueprint('api_actors', __name__, url_prefix="/api/actor")

@bp.route('/')
def index():
    db = get_db()
    actor = db.execute(
        'SELECT first_name,last_name,actor_id'
        ' FROM actor '
        ' ORDER BY first_name,last_name '
    ).fetchall()
    return render_template('actor/index.html', actor = actor)

@bpapi.route('/')
def index_api():
    database = get_db()
    actores = database.execute(
        'SELECT first_name as nombre,last_name as apellido,actor_id'
        ' FROM actor '
        ' ORDER BY nombre,apellido '
    ).fetchall()
    for actor in actores:
        actor["url"] = url_for("api_actores.detalle_api", id=actor["actor_id"], _external=True)
    
    return jsonify(actores=actores)
