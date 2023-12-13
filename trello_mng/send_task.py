import requests
from aiogram.utils.json import json
from trello import TrelloClient

from config.cfg import *


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

    def set_status_field(self, card_id, status=ACTIVE_STATUS_TRELLO):
        url_set_status = f"https://api.trello.com/1/card/{card_id}/customField/{TRELLO_STATUS_FIELD}/item"

        payload = {
            'idValue': status
        }

        return requests.request(
            "PUT",
            url_set_status,
            headers={'Content-Type': 'application/json'},
            params=self.default_key_dict,
            data=json.dumps(payload)
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
        ).json()

    def set_webhook_card(self, card_id):
        query = {
            'callbackURL': f'{TRELLO_BASE_URL}/mt_shop_creo',
            'idModel': card_id,
            'description': f'webhook_card_{card_id}'
        }

        return requests.post(
            self.url_webhook,
            headers={'Content-Type': 'application/json'},
            params=query | self.default_key_dict
        )

    def write_comment_card(self, card, comment):
        url_comment = f"https://api.trello.com/1/cards/{card}/actions/comments"

        return requests.request(
            "POST",
            url_comment,
            params=self.default_key_dict | {"text": comment}
        )

