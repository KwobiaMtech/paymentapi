from typing import List

from Configurations import Configuration
import requests


class PayStack:
    def __init__(self, request: dict):
        self.request = request
        self.url = Configuration.PAYSTACK_API
        self.response = {}
        self.user_response = {}

    def initiate_payment(self):
        headers = PayStack.payStackHeaders()
        sending = self.payStackFormat()
        url = f"{self.url}/charge"
        response = requests.post(url, json=sending, headers=headers)
        self.response = response.json()
        self.user_response = self.userResponse()

    def payStackFormat(self) -> dict:
        # phone = "0551234987" if Configuration.DEBUG is False else self.request["phone"]
        phone = self.request["phone"]
        return {
            "amount": str(int(self.request['amount']) * 10000),
            "email": self.request['email'],
            "reference": self.request["reference"],
            "mobile_money": {"phone": phone, "provider": self.request['provider']}
        }

    def userResponse(self):
        sending = {
            "message": self.response["message"],
            "reference": self.response["data"]["reference"],
            "status": self.response["data"]["status"],
        }
        print('get display_text')
        print(self.response["data"]["display_text"])
        if "display_text" in self.response["data"]:
            sending["display_text"] = self.response["data"]["display_text"]
        return sending

    @staticmethod
    def payStackHeaders() -> dict:
        return {
            "Authorization": f"Bearer {Configuration.PAYSTACK_SECRET_KEY}",
            "Content-Type": "application/json"
        }

    @staticmethod
    def checkStatus(reference):
        url = f'{Configuration.PAYSTACK_API}/transaction/verify/{reference}'
        request_response = requests.get(url, headers=PayStack.payStackHeaders())
        response = request_response.json()
        print('get status response')
        print(response)
        sending = {
            "status": response["data"]["status"] if "data" in response else "not_available",
            "reference": response["data"]["reference"] if "data" in response else reference
        }
        return sending

    @staticmethod
    def chargeValidation(type, data):
        url = f'{Configuration.PAYSTACK_API}/charge/{type}'
        response = requests.post(url, json=data, headers=PayStack.payStackHeaders())
        return response.json()
