import re
import json
import datetime
from culqi.utils.errors import CustomException

class Helpers:

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
        if not string.startswith(start + "_test_") and not string.startswith(start + "_live_"):
            raise CustomException(f'Incorrect format. The format must start with {start}_test_ or {start}_live_')

    def validate_value(value, allowed_values):
        if value not in allowed_values:
            raise CustomException(f'Invalid value. It must be {json.dumps(allowed_values)}.')

    def is_future_date(expiration_date):
        exp_date = datetime.datetime.fromtimestamp(expiration_date)
        return exp_date > datetime.datetime.now()
    
    def validate_date_filter(date_from, date_to):
        _date_from = int(date_from)
        _date_to = int(date_to)
        
        if(_date_to < _date_from):
            raise CustomException('Invalid value. Date_from it must be less than date_to')