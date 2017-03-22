import telegram


class TelegramBotService(object):
    def __init__(self, auth_token):
        self.client = telegram.Bot(auth_token)

    def register(self, url):
        self.client.setWebhook(url)

    def send(self, chat_id, text):
        self.client.sendMessage(chat_id=chat_id, text=text)
