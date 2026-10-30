import json
import os
from flask import Blueprint, jsonify
from core.cache import cache

bp = Blueprint("config", __name__, url_prefix="/Data")

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")


def load_json(filename: str):
    key = f"data:{filename}"
    cached = cache.get(key)
    if cached:
        return cached
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        data = json.load(f)
    cache.set(key, data)
    return data


@bp.route("/ConfigV2", methods=["GET"])
def config_v2():
    data = load_json("config_v2.json")
    if data is None:
        # Minimal default so the client doesn't crash
        data = {"version": 2, "features": {}}
    return jsonify(data)


@bp.route("/GameConfigs", methods=["GET"])
def game_configs():
    data = load_json("game_configs.json")
    if data is None:
        data = []
    return jsonify(data)


@bp.route("/AvatarItems", methods=["GET"])
def avatar_items():
    data = load_json("avatar_items.json")
    if data is None:
        data = []
    return jsonify(data)


@bp.route("/Consumables", methods=["GET"])
def consumables():
    data = load_json("consumables.json")
    if data is None:
        data = []
    return jsonify(data)


@bp.route("/Equipment", methods=["GET"])
def equipment():
    data = load_json("equipment.json")
    if data is None:
        data = []
    return jsonify(data)
