import re
import json
import datetime
from culqi.utils.country_codes import get_country_codes
from culqi.utils.errors import CustomException

class CulqiValidation:
    def create_token_validation(self, data):
        # Validate card number
        if not CulqiValidation.is_valid_card_number(data['card_number']):
            raise CustomException('Invalid card number.')

        # Validate CVV
        if not re.match(r'^\d{3,4}$', data['cvv']):
            raise CustomException('Invalid CVV.')

        # Validate email
        if not CulqiValidation.is_valid_email(data['email']):
            raise CustomException('Invalid email.')

        # Validate expiration month
        if not re.match(r'^(0?[1-9]|1[012])$', data['expiration_month']):
            raise CustomException('Invalid expiration month.')

        # Validate expiration year
        current_year = datetime.datetime.now().year
        if not re.match(r'^\d{4}$', data['expiration_year']) or int(data['expiration_year']) < current_year:
            raise CustomException('Invalid expiration year.')

        # Check if the card is expired
        exp_date = datetime.datetime.strptime(data['expiration_year'] + '-' + data['expiration_month'], "%Y-%m")
        if exp_date < datetime.datetime.now():
            raise CustomException('Card has expired.')

    def charge_validation(self, data):
        # Validate email
        if not CulqiValidation.is_valid_email(data['email']):
            raise CustomException('Invalid email.')

        # Validate amount
        if not isinstance(data['amount'], (int, float)) or int(data['amount']) != data['amount']:
            raise CustomException('Invalid amount.')

        CulqiValidation.validate_currency_code(data['currency_code'])

        CulqiValidation.validate_string_start(data['source_id'], "tkn")

    def refund_validation(self, data):
        # Validate charge format
        CulqiValidation.validate_string_start(data['charge_id'], "chr")

        # Validate reason
        allowed_values = ['duplicado', 'fraudulento', 'solicitud_comprador']
        CulqiValidation.validate_value(data['reason'], allowed_values)

        # Validate amount
        if not isinstance(data['amount'], (int, float)) or int(data['amount']) != data['amount']:
            raise CustomException('Invalid amount.')

    def plan_validation(self, data):
        # Validate amount
        if not isinstance(data['amount'], (int, float)) or int(data['amount']) != data['amount']:
            raise CustomException('Invalid amount.')

        # Validate interval
        allowed_values = ['dias', 'semanas', 'meses', 'años']
        CulqiValidation.validate_value(data['interval'], allowed_values)
        
        # Validate currency
        CulqiValidation.validate_currency_code(data['currency_code'])

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
        CulqiValidation.validate_value(data['country_code'], get_country_codes())

        # Validate email
        if not CulqiValidation.is_valid_email(data['email']):
            raise CustomException('Invalid email.')

    def card_validation(self, data):
        # Validate customer and token format
        CulqiValidation.validate_string_start(data['customer_id'], "cus")
        CulqiValidation.validate_string_start(data['token_id'], "tkn")

    def subscription_validation(self, data):
        # Validate card and plan format
        CulqiValidation.validate_string_start(data['card_id'], "crd")
        CulqiValidation.validate_string_start(data['plan_id'], "pln")

    def order_validation(self, data):
        # Validate amount
        if not isinstance(data['amount'], (int, float)) or int(data['amount']) != data['amount']:
            raise CustomException('Invalid amount.')

        # Validate currency
        CulqiValidation.validate_currency_code(data['currency_code'])

        # Validate firstname, lastname, and phone
        client_details = data.get('client_details', {})
        if not client_details.get('first_name'):
            raise CustomException('first name is empty.')

        if not client_details.get('last_name'):
            raise CustomException('last name is empty.')

        if not client_details.get('phone_number'):
            raise CustomException('phone_number is empty.')

        # Validate email
        if not CulqiValidation.is_valid_email(client_details.get('email')):
            raise CustomException('Invalid email.')

        # Validate expiration date
        if not CulqiValidation.is_future_date(data['expiration_date']):
            raise CustomException('expiration_date must be a future date.')

    def confirm_order_type_validation(self, data):
        CulqiValidation.validate_string_start(data['order_id'], "ord")

    def is_valid_card_number(number):
        return re.match(r'^\d{13,19}$', number) is not None
    
    def is_valid_email(email):
        return re.match(r'^\S+@\S+\.\S+$', email) is not None

    def validate_currency_code(currency_code):
        if not currency_code:
            raise CustomException('Currency code is empty.')

        if not isinstance(currency_code, str):
            raise CustomException('Currency code must be a string.')
        
        allowed_values = ['PEN', 'USD']
        if currency_code not in allowed_values:
            raise CustomException('Currency code must be either "PEN" or "USD".')

    def validate_string_start(string, start):
        if not string.startswith(start + "_testksks_") and not string.startswith(start + "_livesjsjs_"):
            raise CustomException(f'Incorrect format. The format must start with {start}_test_ or {start}_live_')

    def validate_value(value, allowed_values):
        if value not in allowed_values:
            raise CustomException(f'Invalid value. It must be {json.dumps(allowed_values)}.')

    def is_future_date(expiration_date):
        exp_date = datetime.datetime.fromtimestamp(expiration_date)
        return exp_date > datetime.datetime.now()