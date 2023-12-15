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
        if not isinstance(data['amount'], (int, float)) or int(data['amount']) != data['amount']:
            raise CustomException('Invalid amount.')

        Helpers.validate_currency_code(data['currency_code'])

        Helpers.validate_string_start(data['source_id'], "tkn")