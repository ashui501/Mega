import re
from os import environ
from pyrogram import Client
from Script import script 
from aiohttp import ClientSession
from telethon import TelegramClient
from collections import defaultdict
from typing import Dict, List, Union

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_ID = int(environ.get("BOT_ID", 5011611409))
BOT_USERNAME = environ.get("BOT_USERNAME", "VijayFilterTG_BoT")
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled((environ.get('USE_CAPTION_FILTER', 'True')), True)

PICS = (environ.get('PICS', 'https://telegra.ph/file/a66ff1d428ff6640c3b84.mp4')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/46443096bc6895c74a716.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/a66ff1d428ff6640c3b84.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/b58f576fed14cd645d2cf.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
OWNER_ID = int(environ.get('OWNER_ID', 2107036689))
DEV_USERS = environ.get("DEV_USERS", "1794941609 2107036689")
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID')
REQST_CHANNEL = environ.get('REQST_CHANNEL', 'https://t.me/VijayTG_Req')
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = is_enabled((environ.get("NO_RESULTS_MSG", 'False')), False)

# MongoDB information
SQL_DB = environ.get('SQL_DB', 'postgresql://xwzbjnyc:9X_bHyBxh6wHC4_B31hLjprva2PzMXQL@berry.db.elephantsql.com/xwzbjnyc')
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://nivethamaha:nivima@cluster0.ep43gv0.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Nivi")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
IS_VERIFY = is_enabled((environ.get('IS_VERIFY', 'False')), False)
BOTLOG = is_enabled((environ.get('BOTLOG', 'False')), False)
LOGSPAMMER = is_enabled((environ.get('LOGSPAMMER', 'False')), False)
HOW_TO_VERIFY = environ.get('HOW_TO_VERIFY', "https://t.me/c/1845700490/3")
VERIFY2_URL = environ.get('VERIFY2_URL', "mdisklink.link")
VERIFY2_API = environ.get('VERIFY2_API', "4fa150d44b4bf6579c24b33bbbb786dbfb4fc673")
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'clicksfly.com')
SHORTLINK_API = environ.get('SHORTLINK_API', 'c2150e28189cefefd05f8a9c5c5770cc462033e3')
IS_SHORTLINK = is_enabled((environ.get('IS_SHORTLINK', 'False')), False)
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "7")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/VijayTG_Support')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/VijayTG_Updates')
MSG_ALRT = environ.get('MSG_ALRT', 'Wʜᴀᴛ Aʀᴇ Yᴏᴜ Lᴏᴏᴋɪɴɢ Aᴛ ?')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1001653852670))
LOL_CHANNEL = int(environ.get('LOL_CHANNEL', -1001519246187))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'VijayTG_Support')
SUPPORT_GROUP = environ.get('SUPPORT_GROUP', '-1001519246187')
SUPPORT_LINK = environ.get('SUPPORT_LINK', 'https://t.me/+kS3u2kJq1ZZiZDA1')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "False")), False)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CUSTOM_FILE_CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)
TEMP_DOWNLOAD_DIRECTORY = environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")
WOLFRAM_ID = environ.get("WOLFRAM_ID", "")

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

tbot = TelegramClient("naveentg", API_ID, API_HASH)
tbot.start(bot_token=BOT_TOKEN)

Jiraiya = Client("Jiraiya", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Jiraiya"), )

aiohttpsession = ClientSession()

paste_bin_store_s = {
    # "deldog": {
    #   "URL": "https://del.dog/documents",
    #   "GAS": "https://github.com/dogbin/dogbin",
    # },
    "nekobin": {
        "URL": "https://nekobin.com/api/documents",
        "RAV": "result.key",
        "GAS": "https://github.com/nekobin/nekobin",
    },
    "pasty": {
        "URL": "https://pasty.lus.pm/api/v2/pastes",
        "HEADERS": {
            "User-Agent": "PyroGramBot/6.9",
            "Content-Type": "application/json",
        },
        "RAV": "id",
        "GAS": "https://github.com/lus/pasty",
        "AVDTS": "deletionToken",
    },
    "pasting": {
        "URL": "https://pasting.codes/api",
    },
}

#red