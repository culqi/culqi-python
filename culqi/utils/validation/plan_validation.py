import re
import json
import datetime
from culqi.utils.validation.country_codes import get_country_codes
from culqi.utils.errors import CustomException
from culqi.utils.validation.helpers import Helpers

class PlanValidation:
        
    def create(self, data):
        # Validate amount
        if not isinstance(data['amount'], (int, float)) or int(data['amount']) != data['amount']:
            raise CustomException('Invalid amount.')

        # Validate interval
        allowed_values = ['dias', 'semanas', 'meses', 'años']
        Helpers.validate_value(data['interval'], allowed_values)
        
        # Validate currency
        Helpers.validate_currency_code(data['currency_code'])
        
    def retrieve(self, id):
        Helpers.validate_string_start(id, "pln")
        
    def update(self, id):
        Helpers.validate_string_start(id, "pln")
        
    def list(self, data):
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
            
        if 'creation_date_from' in data and 'creation_date_to' in data:
            Helpers.validate_date_filter(data['creation_date_from'], data['creation_date_to'])