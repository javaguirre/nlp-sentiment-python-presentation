import json

import apiai


class ApiAIService():
    def __init__(self, access_token):
        self.client = apiai.ApiAI(access_token)

    def process(self, text):
        request = self.client.text_request()
        request.query = text
        response = request.getresponse()

        response = json.loads(response.read())

        try:
            text = response['result']['fulfillment']['messages'][0]['speech']
        except KeyError:
            print('NLP NOT HANDLED')
            print(response)

        return text
