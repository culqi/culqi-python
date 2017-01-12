import culqipy, json, util
from object import Object

class Charge:

    def create(self, address, address_city, amount, country_code, currency_code, email, first_name, installments, last_name,
                     metadata, phone_number, product_description, token_id):
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
        return util.jsonResult(culqipy.API_KEY, "/charges/", charge.toJSON(), "POST")
