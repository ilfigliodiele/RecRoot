from flask import Blueprint, jsonify
from config.settings import SERVICES

bp = Blueprint("api", __name__, url_prefix="/API")


@bp.route("/services", methods=["GET"])
def services():
    """Return the full service directory — first call the client makes."""
    return jsonify(SERVICES)


@bp.route("/version", methods=["GET"])
def version():
    return jsonify({
        "version": "1.0.0",
        "build": "recroot-2021",
        "status": "ok",
    })
