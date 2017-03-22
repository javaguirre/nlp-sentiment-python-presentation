import time
import os

from flask import Flask, request

from lib.telegram_service import TelegramBotService
from lib.signals import incoming_message_signal
from lib.listeners import ListenerService

app = Flask(__name__)

BASE_URL = os.environ.get('FLASK_BASE_URL', '')
PORT = os.environ.get('PORT', 5000)
WEBHOOK_URI = '/webhook'


def init_app():
    auth_token = os.environ.get('TELEGRAM_AUTH_TOKEN', '')
    url = ''.join([BASE_URL, WEBHOOK_URI])
    TelegramBotService(auth_token).register(url)
    time.sleep(1)


@app.route(WEBHOOK_URI, methods=['POST'])
def webhook():
    post_data = request.get_json()

    # 400 will be raised by default
    # http://flask.pocoo.org/docs/0.12/quickstart/#the-request-object
    message = dict(
        conversation_id=post_data['message']['chat']['id'],
        username=post_data['message']['from']['first_name'],
        text=post_data['message']['text'])

    print('NEW MESSAGE {}'.format(post_data))

    # Send signal
    incoming_message_signal.send(message)

    return 'OK'


if __name__ == "__main__":
    init_app()

    # We connect with the needed signals
    ListenerService(app.config).connect()

    app.run(debug=True, port=PORT)
