from flask import Flask, jsonify
from flask_cors import CORS
from config.settings import PORT, DEBUG, CORS_ORIGINS
from core.rate_limiter import limiter

# --- Route blueprints ---
from routes.api            import bp as api_bp
from routes.auth           import bp as auth_bp
from routes.accounts       import bp as accounts_bp
from routes.config         import bp as config_bp
from routes.rooms          import bp as rooms_bp
from routes.matchmaking    import bp as matchmaking_bp
from routes.player_settings import bp as player_settings_bp
from routes.stub import (
    BugReporting, Cards, CDN, Chat, Clubs, CMS, Commerce,
    DataCollection, Discovery, Econ, GameLogs, Geo, Images,
    Leaderboard, Link, Lists, Moderation, Notifications,
    PlatformNotif, RoomComments, Storage, Strings, StringsCDN,
    Studio, Thorn, Videos,
)


def create_app():
    app = Flask(__name__)
    CORS(app, origins=CORS_ORIGINS)
    limiter.init_app(app)

    # Core blueprints
    app.register_blueprint(api_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(accounts_bp)
    app.register_blueprint(config_bp)
    app.register_blueprint(rooms_bp)
    app.register_blueprint(matchmaking_bp)
    app.register_blueprint(player_settings_bp)

    # Stub blueprints (not yet implemented)
    for stub in [
        BugReporting, Cards, CDN, Chat, Clubs, CMS, Commerce,
        DataCollection, Discovery, Econ, GameLogs, Geo, Images,
        Leaderboard, Link, Lists, Moderation, Notifications,
        PlatformNotif, RoomComments, Storage, Strings, StringsCDN,
        Studio, Thorn, Videos,
    ]:
        app.register_blueprint(stub)

    @app.route("/")
    def index():
        return jsonify({"server": "RecRoot", "status": "running"})

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Not found"}), 404

    @app.errorhandler(429)
    def rate_limited(e):
        return jsonify({"error": "Rate limit exceeded"}), 429

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({"error": "Internal server error"}), 500

    return app


if __name__ == "__main__":
    app = create_app()
    print(f"RecRoot running on http://0.0.0.0:{PORT}")
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
