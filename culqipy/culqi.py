import requests, json
from object import Object

class Culqi:

    API_URL = "https://api.culqi.com/v2"

    def __init__(self, COD_COMMERCE, API_KEY):
        self.COD_COMMERCE = COD_COMMERCE
        self.API_KEY = API_KEY

    def jsonResult(self, url, data):
        headers = {"Authorization": "Bearer "+self.API_KEY, "content-type": "application/json"}
        r = requests.post(self.API_URL+url, headers=headers, data=data)
        return r.json()

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
        return r.json()

    def createCharge(self, address, address_city, amount, country_code, currency_code, email, first_name, installments, last_name,
                     metadata, order_id, phone_number, product_description, token_id):
        charge = Object()
        charge.address = address
        charge.address_city = address_city
        charge.amount = amount
        charge.country_code = country_code
        charge.currency_code = currency_code
        charge.email = email
        charge.first_name = first_name
        charge.installments = installments
        charge.last_name = last_name
        charge.metadata = metadata
        charge.phone_number = phone_number
        charge.product_description = product_description
        charge.token_id = token_id
        return self.jsonResult("/charges/", charge.toJSON())

    def createPlan(self, alias, amount, currency_code, interval, interval_count, limit, name, trial_days):
        plan = Object()
        plan.alias = alias
        plan.amount = amount
        plan.currency_code = currency_code
        plan.interval = interval
        plan.interval_count = interval_count
        plan.limit = limit
        plan.name = name
        plan.trial_days = trial_days
        return self.jsonResult("/plans/", plan.toJSON())

    def createSubscription(self, address, address_city, country_code, email, last_name, first_name, phone_number,
                           plan_alias, token_id):
        subscription = Object()
        subscription.address = address
        subscription.address_city = address_city
        subscription.country_code = country_code
        subscription.email = email
        subscription.last_name = last_name
        subscription.first_name = first_name
        subscription.phone_number = phone_number
        subscription.plan_alias = plan_alias
        subscription.token_id = token_id
        return self.jsonResult("/subscriptions/", subscription.toJSON())

    def createRefund(self, amount, charge_id, reason):
        refund = Object()
        refund.amount = amount
        refund.charge_id = charge_id
        refund.reason = reason
        return self.jsonResult("/refunds/", refund.toJSON())
