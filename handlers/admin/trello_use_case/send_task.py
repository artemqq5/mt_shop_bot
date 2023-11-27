import requests
from trello import TrelloClient

from config.cfg import TRELLO_KEY, TRELLO_TOKEN, TRELLO_SECRET, TRELLO_LIST_CREO_NEW


class TrelloCard:
    def __init__(self, name, desc, date=None):
        self.name = name
        self.desc = desc
        self.date = date


class MyTrelloManager:

    default_key_dict = {'key': TRELLO_KEY, 'token': TRELLO_TOKEN}
    url_card = "https://api.trello.com/1/cards"
    url_webhook = "https://api.trello.com/1/webhooks/"

    def __init__(self):
        self.trello_client = TrelloClient(
            api_key=TRELLO_KEY,
            api_secret=TRELLO_SECRET,
            token=TRELLO_TOKEN
        )

    def generate_task(self, card, labels=None):
        query = {
            'idList': TRELLO_LIST_CREO_NEW,
            'name': card.name,
            'desc': card.desc,
            'idLabels': labels,
            'due': card.date,
        }

        return requests.request(
            "POST",
            url=self.url_card,
            headers={"Accept": "application/json"},
            params=query | self.default_key_dict
        )

    def set_webhook_card(self, card_id):
        query = {
            'key': TRELLO_KEY,
            'token': TRELLO_TOKEN,
            'callbackURL': ' https://2e0a-37-229-228-136.ngrok.io/mt_shop_creo',
            'idModel': card_id,
            'description': f'webhook_card_{card_id}'
        }
        return requests.post(self.url_webhook, params=query)

