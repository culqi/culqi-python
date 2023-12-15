import re
import json
import datetime
from culqi.utils.validation.country_codes import get_country_codes
from culqi.utils.errors import CustomException
from culqi.utils.validation.helpers import Helpers

class CulqiValidation:

    def refund_validation(self, data):
        # Validate charge format
        Helpers.validate_string_start(data['charge_id'], "chr")

        # Validate reason
        allowed_values = ['duplicado', 'fraudulento', 'solicitud_comprador']
        Helpers.validate_value(data['reason'], allowed_values)

        # Validate amount
        if not isinstance(data['amount'], (int, float)) or int(data['amount']) != data['amount']:
            raise CustomException('Invalid amount.')

    def plan_validation(self, data):
        # Validate amount
        if not isinstance(data['amount'], (int, float)) or int(data['amount']) != data['amount']:
            raise CustomException('Invalid amount.')

        # Validate interval
        allowed_values = ['dias', 'semanas', 'meses', 'años']
        Helpers.validate_value(data['interval'], allowed_values)
        
        # Validate currency
        Helpers.validate_currency_code(data['currency_code'])

    def customer_validation(self, data):
        # Validate address, firstname, and lastname
        if not data.get('first_name'):
            raise CustomException('first name is empty.')

        if not data.get('last_name'):
            raise CustomException('last name is empty.')

        if not data.get('address'):
            raise CustomException('address is empty.')

        if not data.get('address_city'):
            raise CustomException('address_city is empty.')

        # Validate country code
        Helpers.validate_value(data['country_code'], get_country_codes())

        # Validate email
        if not Helpers.is_valid_email(data['email']):
            raise CustomException('Invalid email.')

    def card_validation(self, data):
        # Validate customer and token format
        Helpers.validate_string_start(data['customer_id'], "cus")
        Helpers.validate_string_start(data['token_id'], "tkn")

    def subscription_validation(self, data):
        # Validate card and plan format
        Helpers.validate_string_start(data['card_id'], "crd")
        Helpers.validate_string_start(data['plan_id'], "pln")

    def order_validation(self, data):
        # Validate amount
        if not isinstance(data['amount'], (int, float)) or int(data['amount']) != data['amount']:
            raise CustomException('Invalid amount.')

        # Validate currency
        Helpers.validate_currency_code(data['currency_code'])

        # Validate firstname, lastname, and phone
        client_details = data.get('client_details', {})
        if not client_details.get('first_name'):
            raise CustomException('first name is empty.')

        if not client_details.get('last_name'):
            raise CustomException('last name is empty.')

        if not client_details.get('phone_number'):
            raise CustomException('phone_number is empty.')

        # Validate email
        if not Helpers.is_valid_email(client_details.get('email')):
            raise CustomException('Invalid email.')

        # Validate expiration date
        if not Helpers.is_future_date(data['expiration_date']):
            raise CustomException('expiration_date must be a future date.')

    def confirm_order_type_validation(self, data):
        Helpers.validate_string_start(data['order_id'], "ord")
        