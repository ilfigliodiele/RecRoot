import uuid
from flask import Blueprint, jsonify, request, g
from core.auth import require_auth, optional_auth
from core.cache import cache

bp = Blueprint("rooms", __name__, url_prefix="/Rooms")


def get_rooms():
    rooms = cache.get("rooms")
    if rooms is None:
        rooms = {}
        cache.set("rooms", rooms)
    return rooms


@bp.route("", methods=["GET"])
@optional_auth
def list_rooms():
    rooms = get_rooms()
    return jsonify(list(rooms.values()))


@bp.route("/<room_id>", methods=["GET"])
@optional_auth
def get_room(room_id):
    rooms = get_rooms()
    room = rooms.get(room_id)
    if not room:
        return jsonify({"error": "Room not found"}), 404
    return jsonify(room)


@bp.route("/import", methods=["POST"])
@require_auth
def import_room():
    data = request.get_json(silent=True) or {}
    name = data.get("name", "Unnamed Room").strip()
    room_id = str(uuid.uuid4())

    room = {
        "id": room_id,
        "name": name,
        "ownerId": g.user_id,
        "ownerUsername": g.username,
        "playerCount": 0,
        "maxPlayers": data.get("maxPlayers", 20),
        "tags": data.get("tags", []),
    }

    rooms = get_rooms()
    rooms[room_id] = room
    cache.set("rooms", rooms)

    return jsonify(room), 201


@bp.route("/<room_id>", methods=["DELETE"])
@require_auth
def delete_room(room_id):
    rooms = get_rooms()
    room = rooms.get(room_id)
    if not room:
        return jsonify({"error": "Room not found"}), 404
    if room["ownerId"] != g.user_id:
        return jsonify({"error": "Forbidden"}), 403
    del rooms[room_id]
    cache.set("rooms", rooms)
    return jsonify({"ok": True})
