import json

import requests

from private_cfg import WHITE_PAY_SLUG, BOT_LINK, WHITE_PAY_AUTHTOKEN


class WhitePayRepository:

    def __init__(self):
        self.__BASE_URL = "https://api.whitepay.com"
        self.__ORDER_CREATE = f"{self.__BASE_URL}/private-api/crypto-orders/{WHITE_PAY_SLUG}"
        self.__headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': WHITE_PAY_AUTHTOKEN
        }

    def create_invoice(self, sum_invoice):
        payload = json.dumps({
            "amount": str(sum_invoice),
            "currency": "USDT",
            "successful_link": BOT_LINK,
            "failure_link": BOT_LINK
        })

        response = requests.request("POST", self.__ORDER_CREATE, headers=self.__headers, data=payload)
        if not response:
            print(f"create_invoice {response.text}")
            return

        return response.json()


