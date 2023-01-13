import configparser

config = configparser.ConfigParser()
config.read("config.ini")

TELEGRAM_API_ID = config['Telegram']['api_id']
TELEGRAM_API_HASH = config['Telegram']['api_hash']
TELEGRAM_PHONE_NUMBER = config['Telegram']['phone_number']

API_URL = config['Api']['url']
API_KEY = config['Api']['key']
