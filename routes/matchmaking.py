from flask import Blueprint, jsonify, request, g
from core.auth import require_auth
from core.cache import cache

bp = Blueprint("matchmaking", __name__, url_prefix="/Matchmaking")


@bp.route("/find", methods=["POST"])
@require_auth
def find_match():
    data = request.get_json(silent=True) or {}
    room_tag = data.get("tag", "")

    rooms = cache.get("rooms") or {}
    available = [
        r for r in rooms.values()
        if r["playerCount"] < r["maxPlayers"]
        and (not room_tag or room_tag in r.get("tags", []))
    ]

    if not available:
        return jsonify({"error": "No rooms available"}), 404

    # Return first available room (improve with proper matchmaking logic)
    return jsonify(available[0])


@bp.route("/join/<room_id>", methods=["POST"])
@require_auth
def join_room(room_id):
    rooms = cache.get("rooms") or {}
    room = rooms.get(room_id)
    if not room:
        return jsonify({"error": "Room not found"}), 404
    if room["playerCount"] >= room["maxPlayers"]:
        return jsonify({"error": "Room is full"}), 409

    room["playerCount"] += 1
    cache.set("rooms", rooms)
    return jsonify({"ok": True, "room": room})


@bp.route("/leave/<room_id>", methods=["POST"])
@require_auth
def leave_room(room_id):
    rooms = cache.get("rooms") or {}
    room = rooms.get(room_id)
    if not room:
        return jsonify({"error": "Room not found"}), 404

    room["playerCount"] = max(0, room["playerCount"] - 1)
    cache.set("rooms", rooms)
    return jsonify({"ok": True})
