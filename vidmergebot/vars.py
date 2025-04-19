from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Vars:
    CACHE_TIME = int(config("CACHE_TIME", default=5))
    DOWN_PATH = f"{getcwd()}/vidmergebot/downloads"
    BOT_TOKEN = config("BOT_TOKEN", "7651012082:AAFVqWXSI3tBaq8igfQehzBNnP9hfCVwhPw")
    BOT_ID = BOT_TOKEN.split(":")[0]
    APP_ID = int(config("API_ID", "26649585"))
    API_HASH = config("API_HASH", "588a3ea6fd01ae88bd2e10fed7d55b2c")
    WORKERS = int(config("WORKERS", default=16))
    STREAMTAPE_API_PASS = config("STREAMTAPE_API_PASS", "Rahat@146@")
    STREAMTAPE_API_USERNAME = config("STREAMTAPE_API_USERNAME", "2be20901e8e197f56a03")
    MESSAGE_DUMP = int(config("MESSAGE_DUMP", "-1002571138456"))
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/ !").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="RM-Supports")
    AUTH_CHANNEL = config("AUTH_CHANNEL", default=-1002323154734)
    OWNER_ID = int(config("OWNER_ID", default=7822720438))
    CAPTION = config("CAPTION", default="By @MLTBRM")
    VERSION = config("VERSION", default="v1.1 - Stable")
    STREAMTAPE_DEFAULT = config("STREAMTAPE_DEFAULT", default=None, cast=config.boolean)
    BOT_USERNAME = config("BOT_USERNAME", "Merge_smbot")
    DB_URI = config("DB_URI", "mongodb+srv://rohanahamed75:gt4RXJZ1mUtOh4Xv@mmtg.0ong5.mongodb.net/?retryWrites=true&w=majority&appName=mmtg")
    MAX_VIDEOS = int(config("MAX_VIDEOS", default=10))
    JOIN_CHECK = config("JOIN_CHECK", default=None, cast=config.boolean)
    MAX_NON_JOIN_USAGE = int(config("MAX_NON_JOIN_USAGE", default=2))
    MAX_JOIN_USAGE = int(config("MAX_JOIN_USAGE", default=2))
    LIMIT_USER_USAGE = config("LIMIT_USER_USAGE", default=None, cast=config.boolean)
