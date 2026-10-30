from flask import Blueprint, jsonify, g
from core.auth import require_auth
from core.cache import cache

bp = Blueprint("accounts", __name__, url_prefix="/Accounts")


def get_users():
    return cache.get("users") or {}


@bp.route("/me", methods=["GET"])
@require_auth
def me():
    users = get_users()
    user = next((u for u in users.values() if u["id"] == g.user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({
        "id": user["id"],
        "username": user["username"],
        "displayName": user["username"],
        "level": 1,
        "xp": 0,
        "tokens": 0,
    })


@bp.route("/<user_id>", methods=["GET"])
@require_auth
def get_account(user_id):
    users = get_users()
    user = next((u for u in users.values() if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({
        "id": user["id"],
        "username": user["username"],
        "displayName": user["username"],
        "level": 1,
        "xp": 0,
    })
