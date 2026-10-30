"""
Stub blueprints for services not yet implemented.
Each returns a minimal valid response so the client doesn't crash on startup.
"""
from flask import Blueprint, jsonify


def make_stub(name: str, prefix: str):
    bp = Blueprint(name, __name__, url_prefix=f"/{prefix}")

    @bp.route("/", methods=["GET", "POST"], strict_slashes=False)
    @bp.route("/<path:subpath>", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
    def catch_all(subpath=""):
        return jsonify({"status": "stub", "service": prefix, "path": subpath}), 200

    return bp


BugReporting   = make_stub("bug_reporting",    "BugReporting")
Cards          = make_stub("cards",            "Cards")
CDN            = make_stub("cdn",              "CDN")
Chat           = make_stub("chat",             "Chat")
Clubs          = make_stub("clubs",            "Clubs")
CMS            = make_stub("cms",              "CMS")
Commerce       = make_stub("commerce",         "Commerce")
DataCollection = make_stub("data_collection",  "DataCollection")
Discovery      = make_stub("discovery",        "Discovery")
Econ           = make_stub("econ",             "Econ")
GameLogs       = make_stub("game_logs",        "GameLogs")
Geo            = make_stub("geo",              "Geo")
Images         = make_stub("images",           "Images")
Leaderboard    = make_stub("leaderboard",      "Leaderboard")
Link           = make_stub("link",             "Link")
Lists          = make_stub("lists",            "Lists")
Moderation     = make_stub("moderation",       "Moderation")
Notifications  = make_stub("notifications",    "Notifications")
PlatformNotif  = make_stub("platform_notif",   "PlatformNotifications")
RoomComments   = make_stub("room_comments",    "RoomComments")
Storage        = make_stub("storage",          "Storage")
Strings        = make_stub("strings",          "Strings")
StringsCDN     = make_stub("strings_cdn",      "StringsCDN")
Studio         = make_stub("studio",           "Studio")
Thorn          = make_stub("thorn",            "Thorn")
Videos         = make_stub("videos",           "Videos")
