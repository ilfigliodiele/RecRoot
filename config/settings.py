import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST", "http://localhost:5000")
PORT = int(os.getenv("PORT", 5000))
DEBUG = os.getenv("DEBUG", "true").lower() == "true"

JWT_SECRET = os.getenv("JWT_SECRET", "recroot-dev-secret-change-in-production")
JWT_ALGORITHM = "HS256"
JWT_EXPIRY_HOURS = 24 * 7  # 1 week

RATE_LIMIT_DEFAULT = "200 per minute"
RATE_LIMIT_AUTH = "10 per minute"

CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*")

SERVICES = {
    "Accounts":             f"{HOST}/Accounts",
    "API":                  f"{HOST}/API",
    "Auth":                 f"{HOST}/Auth",
    "BugReporting":         f"{HOST}/BugReporting",
    "Cards":                f"{HOST}/Cards",
    "CDN":                  f"{HOST}/CDN",
    "Chat":                 f"{HOST}/Chat",
    "Clubs":                f"{HOST}/Clubs",
    "CMS":                  f"{HOST}/CMS",
    "Commerce":             f"{HOST}/Commerce",
    "Data":                 f"{HOST}/Data",
    "DataCollection":       f"{HOST}/DataCollection",
    "Discovery":            f"{HOST}/Discovery",
    "Econ":                 f"{HOST}/Econ",
    "GameLogs":             f"{HOST}/GameLogs",
    "Geo":                  f"{HOST}/Geo",
    "Images":               f"{HOST}/Images",
    "Leaderboard":          f"{HOST}/Leaderboard",
    "Link":                 f"{HOST}/Link",
    "Lists":                f"{HOST}/Lists",
    "Matchmaking":          f"{HOST}/Matchmaking",
    "Moderation":           f"{HOST}/Moderation",
    "Notifications":        f"{HOST}/Notifications",
    "PlatformNotifications":f"{HOST}/PlatformNotifications",
    "PlayerSettings":       f"{HOST}/PlayerSettings",
    "RoomComments":         f"{HOST}/RoomComments",
    "Rooms":                f"{HOST}/Rooms",
    "Storage":              f"{HOST}/Storage",
    "Strings":              f"{HOST}/Strings",
    "StringsCDN":           f"{HOST}/StringsCDN",
    "Studio":               f"{HOST}/Studio",
    "Thorn":                f"{HOST}/Thorn",
    "Videos":               f"{HOST}/Videos",
    "WWW":                  HOST,
}
