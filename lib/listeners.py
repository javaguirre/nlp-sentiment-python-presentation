import os

from termcolor import colored, cprint

from lib.apiai_client import ApiAIService
from lib.telegram_service import TelegramBotService
from lib.sentiment import SentimentService
from lib.signals import processed_message_signal, incoming_message_signal


APIAI_ACCESS_TOKEN = os.environ.get('APIAI_ACCESS_TOKEN', '')
TELEGRAM_AUTH_TOKEN = os.environ.get('TELEGRAM_AUTH_TOKEN', '')


def connect_nlp(message):
    client = ApiAIService(APIAI_ACCESS_TOKEN)
    response = client.process(message['text'])
    processed_message_signal.send(dict(message=message, response=response))

    if response:
        print('NLP: {}'.format(response))
    else:
        cprint(colored(
            'NLP ERROR: {} response is not handled by the NLP'.format('response'),
            'red'))

    return response


def connect_telegram(data):
    if not data['response']:
        return

    response = TelegramBotService(TELEGRAM_AUTH_TOKEN).send(
        data['message']['conversation_id'],
        data['response'])

    cprint(colored('TELEGRAM: `{}` sent'.format(data['response'])), 'blue')

    return response


def connect_sentiment(message):
    sentiment = SentimentService()
    response = sentiment.analyze(message['text'])

    print('SENTIMENT: {}'.format(response))

    return response


class ListenerService:
    def __init__(self, config):
        self.config = config

    def connect(self):
        self.connect_incoming_message_signals()
        self.connect_processed_message_signals()

    def connect_incoming_message_signals(self):
        incoming_message_signal.connect(connect_nlp)
        incoming_message_signal.connect(connect_sentiment)

    def connect_processed_message_signals(self):
        processed_message_signal.connect(connect_telegram)
