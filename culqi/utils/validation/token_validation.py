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
        if not re.match(r'^\d{4}$', str(data['expiration_year'])) or int(str(data['expiration_year'])) < current_year:
            raise CustomException('Invalid expiration year.')

        # Check if the card is expired
        exp_date = datetime.datetime.strptime(str(data['expiration_year']) + '-' + str(data['expiration_month']), "%Y-%m")
        if exp_date < datetime.datetime.now():
            raise CustomException('Card has expired.')
        
    def create_token_yape_validation(self, data):
        # Validate amount
        amount = data['amount']
        if isinstance(amount, str):
            try:
                amount = int(amount)
            except CustomException:
                raise CustomException("Invalid 'amount'. It should be an integer or a string representing an integer.")

        if not isinstance(amount, int):
            raise CustomException("Invalid 'amount'. It should be an integer or a string representing an integer.")
    
    def token_retrieve_validation(self, id):
        Helpers.validate_string_start(id, "tkn")
        
    def token_update_validation(self, id):
        Helpers.validate_string_start(id, "tkn")
        
    def token_list_validation(self, data):
        if 'device_type' in data:
            allowed_device_values = ['desktop', 'mobile', 'tablet']
            Helpers.validate_value(data['device_type'], allowed_device_values)
            
        if 'card_brand' in data:
            allowed_brand_values = ['Visa', 'Mastercard', 'Amex', 'Diners']
            Helpers.validate_value(data['card_brand'], allowed_brand_values)
        
        if 'card_type' in data:
            allowed_card_type_values = ['credito', 'debito', 'internacional']
            Helpers.validate_value(data['card_type'], allowed_card_type_values)
        
        if 'country_code' in data:
            Helpers.validate_value(data['country_code'], get_country_codes())
        
        if 'creation_date_from' in data and 'creation_date_to' in data:
            Helpers.validate_date_filter(data['creation_date_from'], data['creation_date_to'])