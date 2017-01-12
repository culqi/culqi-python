import culqipy, requests, json
from object import Object

class Token:

    def create(self, card_number, currency_code, cvv, exp_month, exp_year, fingerprint, last_name, email, first_name):
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
        headers = {"Authorization": "Code "+culqipy.COD_COMMERCE, "content-type": "application/json"}
        r = requests.post(culqipy.API_URL+"/tokens/", headers=headers, data=token.toJSON(), timeout=60)
        return r.json()
