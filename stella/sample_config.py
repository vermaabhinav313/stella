# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.

import os

# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "YOUR BOT TOKEN HERE"
    OWNER_ID = "YOUR OWN ID HERE"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "YOUR USERNAME HERE"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'sqldbtype://username:pw@hostname:port/db_name'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    GBAN_LOGS = None
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    #ID Seperation format [1,2,3,4]
    SUDO_USERS = []
    DEV_USERS = []
    SUPPORT_USERS = []
    WHITELIST_USERS = []
    SPAMMERS = None
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    STRICT_GMUTE = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAACAgUAAxkBAAIHsl5nbqXdDTmpG2HFDNhnwvE5kFbWAAI9AQAC3pTNLzeTCUmnhTneGAQ'  # banhammer marie sticker
    ALLOW_EXCL = True  # Allow ! commands as well as /
    CASH_API_KEY = None # Get one from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = ' ' # Get one from https://timezonedb.com/register



    


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
