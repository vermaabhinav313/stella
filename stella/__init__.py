import logging
import os
import sys
import time

import telegram.ext as tg
from dotenv import load_dotenv
from sys import version_info
StartTime = time.time()



logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)

LOGGER.info("Starting stella...")

load_dotenv("config.env")


# Check if the config was edited by using the already used variable
CONFIG_CHECK = os.environ.get(
    "___________PLOX_______REMOVE_____THIS_____LINE__________", None)

if CONFIG_CHECK:
    LOGS.error("Please remove the line mentioned in the first \
         hashtag from the config.env file")
    quit(1)


if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error("You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting.")
    quit(1)

TOKEN = os.environ.get("API_KEY", None)
OWNER_ID = os.environ.get('OWNER_ID',None)
OWNER_USERNAME = os.environ.get('OWNER_USERNAME',None)
SUDO_USERS = os.environ.get('SUDO_USERS', None)
DEV_USERS = os.environ.get('DEV_USERS',None)
WHITELIST_USERS = os.environ.get('WHITELIST_USERS',None)
SUPPORT_USERS = os.environ.get('SUPPORT_USERS',None)
SPAMMERS = os.environ.get('SPAMMERS',None)
WORKERS = int(os.environ.get('WORKERS', 8))
ALLOW_EXCL = os.environ.get('ALLOW_EXCL', False)
DB_URI = os.environ.get('SQLALCHEMY_DATABASE_URI',None)
WEBHOOK = bool(os.environ.get('WEBHOOK', False))
URL = os.environ.get('URL', "")  # Does not contain token
PORT = int(os.environ.get('PORT', 5000))
CERT_PATH = os.environ.get("CERT_PATH")

LOAD = []
NO_LOAD = ['translation', 'rss']

DEL_CMDS = bool(os.environ.get('DEL_CMDS', False))

MESSAGE_DUMP = os.environ.get('MESSAGE_DUMP', None)
GBAN_LOGS = os.environ.get('GBAN_LOGS', None)
BAN_STICKER = os.environ.get('BAN_STICKER', 'CAACAgUAAxkBAAIHsl5nbqXdDTmpG2HFDNhnwvE5kFbWAAI9AQAC3pTNLzeTCUmnhTneGAQ')

STRICT_GBAN = bool(os.environ.get('STRICT_GBAN', False))
STRICT_GMUTE = bool(os.environ.get('STRICT_GMUTE', False))

CASH_API_KEY = os.environ.get('CASH_API_KEY', None)
TIME_API_KEY = os.environ.get('TIME_API_KEY', None)



updater = tg.Updater(TOKEN, workers=WORKERS)
dispatcher = updater.dispatcher

SUDO_USERS = list(SUDO_USERS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)
WHITELIST_USERS = list(WHITELIST_USERS)
SUPPORT_USERS = list(SUPPORT_USERS)
SPAMMERS = list(SPAMMERS)

# Load at end to ensure all prev variables have been set
from stella.modules.helper_funcs.handlers import CustomCommandHandler, CustomRegexHandler, CustomMessageHandler

# make sure the regex handler can take extra kwargs
tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler

def spamfilters(text, user_id, chat_id):
    #print("{} | {} | {}".format(text, user_id, chat_id))
    if int(user_id) in SPAMMERS:
        print("This user is a spammer!")
        return True
    else:
        return False
