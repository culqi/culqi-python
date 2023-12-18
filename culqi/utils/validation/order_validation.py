import re
import json
import datetime
from culqi.utils.validation.country_codes import get_country_codes
from culqi.utils.errors import CustomException
from culqi.utils.validation.helpers import Helpers

class OrderValidation:
        
    def create(self, data):
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
        
    def retrieve(self, id):
        Helpers.validate_string_start(id, "ord")
        
    def update(self, id):
        Helpers.validate_string_start(id, "ord")
    
    def confirm(self, id):
        Helpers.validate_string_start(id, "ord")
    
    def confirm_type(self, data):
        Helpers.validate_string_start(data['order_id'], "ord")
        
    def list(self, data):
        if 'amount' in data:
            if not isinstance(data['amount'], (int)) or int(data['amount']) != data['amount']:
                raise CustomException('Invalid amount.')
        if 'min_amount' in data:
            if not isinstance(data['min_amount'], (int)) or int(data['min_amount']) != data['min_amount']:
                raise CustomException('Invalid min amount.')
        if 'max_amount' in data:
            if not isinstance(data['max_amount'], (int)) or int(data['max_amount']) != data['max_amount']:
                raise CustomException('Invalid max amount.')
        
        if 'creation_date_from' in data and 'creation_date_to' in data:
            Helpers.validate_date_filter(data['creation_date_from'], data['creation_date_to'])
        