import os


class Config(object):
    BASE_URL = os.environ.get('FLASK_BASE_URL', '')
    DEBUG = False

    PORT = os.environ.get('PORT', 5000)
    WEBHOOK_PATH = '/webhook'
    WEBHOOK_URL = ''.join([BASE_URL, WEBHOOK_PATH])

    APIAI_ACCESS_TOKEN = os.environ.get('APIAI_ACCESS_TOKEN', '')
    TELEGRAM_AUTH_TOKEN = os.environ.get('TELEGRAM_AUTH_TOKEN', '')
