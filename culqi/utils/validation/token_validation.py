import re
import json
import datetime
from culqi.utils.validation.country_codes import get_country_codes
from culqi.utils.errors import CustomException
from culqi.utils.validation.helpers import Helpers

class TokenValidation:
    def create_token_validation(self, data):
        # Validate card number
        if not Helpers.is_valid_card_number(data['card_number']):
            raise CustomException('Invalid card number.')

        # Validate CVV
        if not re.match(r'^\d{3,4}$', data['cvv']):
            raise CustomException('Invalid CVV.')

        # Validate email
        if not Helpers.is_valid_email(data['email']):
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
        
    def create_token_yape_validation(self, data):
        # Validate amount
        if not isinstance(data['amount'], (int, float)) or int(data['amount']) != data['amount']:
            raise CustomException('Invalid amount.')
    
    def token_retrieve_validation(self, id):
        Helpers.validate_string_start(id, "tkn")
        
    def token_list_validation(self, data):
        allowed_device_values = ['desktop', 'mobile', 'tablet']
        Helpers.validate_value(data['device_type'], allowed_device_values)
        
        allowed_brand_values = ['Visa', 'Mastercard', 'Amex', 'Diners']
        Helpers.validate_value(data['card_brand'], allowed_brand_values)
        
        allowed_card_type_values = ['credito', 'debito', 'internacional']
        Helpers.validate_value(data['card_type'], allowed_card_type_values)
        
        Helpers.validate_value(data['country_code'], get_country_codes())
        
        Helpers.validate_date_filter(data['creation_date_from'], data['creation_date_to'])