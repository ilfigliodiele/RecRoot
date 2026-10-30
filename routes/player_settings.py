from flask import Blueprint, jsonify, request, g
from core.auth import require_auth
from core.cache import cache

bp = Blueprint("player_settings", __name__, url_prefix="/PlayerSettings")


def get_settings(user_id):
    return cache.get(f"settings:{user_id}") or {}


@bp.route("", methods=["GET"])
@require_auth
def get():
    return jsonify(get_settings(g.user_id))


@bp.route("", methods=["POST", "PUT"])
@require_auth
def update():
    data = request.get_json(silent=True) or {}
    current = get_settings(g.user_id)
    current.update(data)
    cache.set(f"settings:{g.user_id}", current)
    return jsonify(current)
