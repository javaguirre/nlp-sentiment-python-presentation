import time
import os

from flask import Flask, request

from lib.telegram_service import TelegramBotService
from lib.signals import incoming_message_signal
from lib.listeners import ListenerService

app = Flask(__name__)
app.config.from_object('settings.Config')


def init_app():
    config = app.config
    TelegramBotService(config['TELEGRAM_AUTH_TOKEN']).register(config['WEBHOOK_URL'])
    time.sleep(1)


@app.route(app.config['WEBHOOK_PATH'], methods=['POST'])
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
    incoming_message_signal.send(message, config=app.config)

    return 'OK'


if __name__ == "__main__":
    init_app()

    # We connect with the needed signals
    ListenerService(app.config).connect()

    app.run(debug=True, port=app.config['PORT'])
