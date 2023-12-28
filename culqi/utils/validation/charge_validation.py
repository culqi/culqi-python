import re
import json
import datetime
from culqi.utils.validation.country_codes import get_country_codes
from culqi.utils.errors import CustomException
from culqi.utils.validation.helpers import Helpers

class ChargeValidation:
        
    def create(self, data):
        # Validate email
        if not Helpers.is_valid_email(data['email']):
            raise CustomException('Invalid email.')

        # Validate amount
        amount = data['amount']
        if isinstance(amount, str):
            try:
                amount = int(amount)
            except CustomException:
                raise CustomException("Invalid 'amount'. It should be an integer or a string representing an integer.")

        if not isinstance(amount, int):
            raise CustomException("Invalid 'amount'. It should be an integer or a string representing an integer.")

        Helpers.validate_currency_code(data['currency_code'])
        
        if data['source_id'].startswith("tkn"):
            Helpers.validate_string_start(data['source_id'], "tkn")
        elif data['source_id'].startswith("ype"):
            Helpers.validate_string_start(data['source_id'], "ype")
        elif data['source_id'].startswith("crd"):
            Helpers.validate_string_start(data['source_id'], "crd")
        else:
            raise CustomException(f'Incorrect format. The format must start with tkn, ype or crd')
        
    def retrieve(self, id):
        Helpers.validate_string_start(id, "chr")
        
    def update(self, id):
        Helpers.validate_string_start(id, "chr")
        
    def capture(self, id):
        Helpers.validate_string_start(id, "chr")
        
    def list(self, data):
         # Validate email
        if 'email' in data:
            if not Helpers.is_valid_email(data['email']):
                raise CustomException('Invalid email.')
        # Validate amount
        if 'amount' in data:
            if not isinstance(data['amount'], (int)) or int(data['amount']) != data['amount']:
                raise CustomException('Invalid amount.')
        if 'min_amount' in data:
            if not isinstance(data['min_amount'], (int)) or int(data['min_amount']) != data['min_amount']:
                raise CustomException('Invalid min amount.')
        if 'max_amount' in data:
            if not isinstance(data['max_amount'], (int)) or int(data['max_amount']) != data['max_amount']:
                raise CustomException('Invalid max amount.')
        if 'installments' in data:
            if not isinstance(data['installments'], (int)) or int(data['installments']) != data['installments']:
                raise CustomException('Invalid installments.')
        if 'min_installments' in data:
            if not isinstance(data['min_installments'], (int)) or int(data['min_installments']) != data['min_installments']:
                raise CustomException('Invalid min installments.')
        if 'max_installments' in data:
            if not isinstance(data['max_installments'], (int)) or int(data['max_installments']) != data['max_installments']:
                raise CustomException('Invalid max installments.')
            
        if 'currency_code' in data:
            Helpers.validate_currency_code(data['currency_code'])
        
        if 'card_brand' in data:
            allowed_brand_values = ['Visa', 'Mastercard', 'Amex', 'Diners']
            Helpers.validate_value(data['card_brand'], allowed_brand_values)
        
        if 'card_type' in data:
            allowed_card_type_values = ['credito', 'debito', 'internacional']
            Helpers.validate_value(data['card_type'], allowed_card_type_values)
        
        if 'creation_date_from' in data and 'creation_date_to' in data:
            Helpers.validate_date_filter(data['creation_date_from'], data['creation_date_to'])
        
        if 'country_code' in data:
            Helpers.validate_value(data['country_code'], get_country_codes())