import requests, json
from object import Object

class Culqi:

    API_URL = "https://api.culqi.com/v2"

    def __init__(self, COD_COMMERCE, API_KEY):
        self.COD_COMMERCE = COD_COMMERCE
        self.API_KEY = API_KEY

    def createToken(self, card_number, currency_code, cvv, exp_month, exp_year, fingerprint, last_name, email, first_name):
        token = Object()
        token.card_number = card_number
        token.currency_code = currency_code
        token.cvv = cvv
        token.expiration_month = exp_month
        token.expiration_year = exp_year
        token.fingerprint = fingerprint
        token.last_name = last_name
        token.email = email
        token.first_name = first_name
        headers = {"Authorization": "Code "+self.COD_COMMERCE, "content-type": "application/json"}
        r = requests.post(self.API_URL+"/tokens/", headers=headers, data=token.toJSON())
        return r.content
