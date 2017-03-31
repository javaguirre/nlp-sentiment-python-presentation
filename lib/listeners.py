import logging

from lib.apiai_client import ApiAIService
from lib.telegram_service import TelegramBotService
from lib.sentiment import SentimentService
from lib.signals import processed_message_signal, incoming_message_signal


def connect_nlp(message, config):
    client = ApiAIService(config['APIAI_ACCESS_TOKEN'])
    response = client.process(message['text'])
    processed_message_signal.send(
        dict(message=message, response=response),
        config=config)

    if response:
        print('NLP: {}'.format(response))
    else:
        logging.info(
            'NLP ERROR: {} response not handled by the NLP'.format('response'))

    return response


def connect_telegram(data, config):
    if not data['response']:
        return

    response = TelegramBotService(config['TELEGRAM_AUTH_TOKEN']).send(
        data['message']['conversation_id'],
        data['response'])

    logging.info('TELEGRAM: `{}` sent'.format(data['response']))

    return response


def connect_sentiment(message, **kwargs):
    sentiment = SentimentService()
    response = sentiment.analyze(message['text'])

    logging.info('SENTIMENT: {}'.format(response))

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
