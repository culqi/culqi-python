import culqipy, json, util
from object import Object

class Subscription:

    def create(self, address, address_city, country_code, email, last_name, first_name, phone_number, plan_alias, token_id):
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
        return util.jsonResult(culqipy.API_KEY, "/subscriptions/", subscription.toJSON(), "POST")
