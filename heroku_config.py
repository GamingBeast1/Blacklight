import os


class Var(object):
    APP_ID = int(os.environ.get("APP_ID", "1848509"))
    # 6 is a placeholder
    API_HASH = os.environ.get("API_HASH", "dd51a36a6bb43c9b9b2824f3bbdcc797")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOLcBuyOLdqm5M4NIBVLJnSgUDnIhbwgAlfZsk2Z5P0JqwV-JPAP7Yr5mMmSeoZgIcnCagE9mr4tRm_jYK9Jm9ESbQzHajO2Iwrg1YB-Ufoa9UxYYS87nV7tgNCvxtFWAy84PuYDZH-US-w8d1AXiWQtz2zr3qhKSCsAvbiw4vP0V5BVJKn52t8b7LniT8B4uWlMmHhrqYmX9NYH-uVcL5K0k5zyuChC7b68ZBmpimzOkCEEkB3GnUT9HBdx__P0TKI0wYYIhVegYM1Lo4Gte1kijFyybqcoS5qX9raVNdCAN0S26H6jYh5oWxbaZbElLgYV0rs9w0ewe4y1zz5sw2UxNJ_M=")
    DB_URI = os.environ.get("DATABASE_URL", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", None)
    LOGGER = True
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    # Here for later purposes
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
    LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
    LESS_SPAMMY = os.environ.get("LESS_SPAMMY", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
    # Send .get_id in any channel to fill this value.
    PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL", "-4282837820"))
    PRIVATE_GROUP_BOT_API_ID = int(os.environ.get("PRIVATE_GROUP_BOT_API_ID", "-4282837820"))
    PM_PERMIT_GROUP_ID = os.environ.get("PM_PERMIT_GROUP_ID", "-4282837820")
    TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
    NO_SONGS = bool(os.environ.get("NO_SONGS", False))
    DOWNLOAD_PFP_URL_CLOCK = os.environ.get("DOWNLOAD_PFP_URL_CLOCK", None)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    MAX_FLOOD_IN_P_M_s = int(os.environ.get("MAX_FLOOD_IN_P_M_s", 3))
    if AUTH_TOKEN_DATA is not None:
        if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
            os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
        t_file = open(TEMP_DOWNLOAD_DIRECTORY + "auth_token.txt", "w")
        t_file.write(AUTH_TOKEN_DATA)
        t_file.close()
    PRIVATE_GROUP_ID = os.environ.get("PRIVATE_GROUP_ID", "-4282837820")
    if PRIVATE_GROUP_ID is not None:
        try:
            PRIVATE_GROUP_ID = int(PRIVATE_GROUP_ID)
        except ValueError:
            raise ValueError(
                "Invalid Private Group ID. Make sure your ID is starts with -100 and make sure that it is only numbers."
            )
    NEWS_CHANNEL_ID = int(os.environ.get("NEWS_CHANNEL_ID", -100))
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
    ANTISPAM_SYSTEM = os.environ.get("ANTISPAM_SYSTEM", "DISABLE")
    LIGHTNING_PRO = os.environ.get("LIGHTNING_PRO", "YES")
    WHITE_CHAT = set(int(x) for x in os.environ.get("WHITE_CHAT", "").split())


class Development(Var):
    LOGGER = True
