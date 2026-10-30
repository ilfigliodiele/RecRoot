import jwt
import datetime
from functools import wraps
from flask import request, jsonify, g
from config.settings import JWT_SECRET, JWT_ALGORITHM, JWT_EXPIRY_HOURS


def generate_token(user_id: str, username: str) -> str:
    """Generate a JWT token for the given user."""
    payload = {
        "sub": user_id,
        "username": username,
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=JWT_EXPIRY_HOURS),
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decode_token(token: str) -> dict:
    """Decode and validate a JWT token. Raises on failure."""
    return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])


def require_auth(f):
    """Decorator: protect an endpoint with JWT auth."""
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing or invalid Authorization header"}), 401
        token = auth_header.split(" ", 1)[1]
        try:
            payload = decode_token(token)
            g.user_id = payload["sub"]
            g.username = payload["username"]
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401
        return f(*args, **kwargs)
    return decorated


def optional_auth(f):
    """Decorator: parse token if present, but don't block if missing."""
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        g.user_id = None
        g.username = None
        if auth_header.startswith("Bearer "):
            token = auth_header.split(" ", 1)[1]
            try:
                payload = decode_token(token)
                g.user_id = payload["sub"]
                g.username = payload["username"]
            except jwt.InvalidTokenError:
                pass
        return f(*args, **kwargs)
    return decorated
