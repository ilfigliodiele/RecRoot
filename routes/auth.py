import uuid
from flask import Blueprint, request, jsonify
from core.auth import generate_token
from core.cache import cache
from core.rate_limiter import limiter

bp = Blueprint("auth", __name__, url_prefix="/Auth")

# In-memory user store (replace with DB later)
def get_users():
    users = cache.get("users")
    if users is None:
        users = {}
        cache.set("users", users)
    return users


@bp.route("/login", methods=["POST"])
@limiter.limit("10 per minute")
def login():
    data = request.get_json(silent=True) or {}
    username = data.get("username", "").strip()
    password = data.get("password", "").strip()

    if not username or not password:
        return jsonify({"error": "username and password required"}), 400

    users = get_users()
    user = users.get(username.lower())

    if not user or user["password"] != password:
        return jsonify({"error": "Invalid credentials"}), 401

    token = generate_token(user["id"], user["username"])
    return jsonify({
        "access_token": token,
        "token_type": "Bearer",
        "user_id": user["id"],
        "username": user["username"],
    })


@bp.route("/register", methods=["POST"])
@limiter.limit("5 per minute")
def register():
    data = request.get_json(silent=True) or {}
    username = data.get("username", "").strip()
    password = data.get("password", "").strip()

    if not username or not password:
        return jsonify({"error": "username and password required"}), 400
    if len(username) < 3 or len(username) > 20:
        return jsonify({"error": "username must be 3-20 characters"}), 400

    users = get_users()
    if username.lower() in users:
        return jsonify({"error": "Username already taken"}), 409

    user_id = str(uuid.uuid4())
    users[username.lower()] = {
        "id": user_id,
        "username": username,
        "password": password,  # TODO: hash passwords
    }
    cache.set("users", users)

    token = generate_token(user_id, username)
    return jsonify({
        "access_token": token,
        "token_type": "Bearer",
        "user_id": user_id,
        "username": username,
    }), 201
