import re
import json
import datetime
from culqi.utils.validation.country_codes import get_country_codes
from culqi.utils.errors import CustomException
from culqi.utils.validation.helpers import Helpers

class CardValidation:
        
    def create(self, data):
        # Validate customer and token format
        Helpers.validate_string_start(data['customer_id'], "cus")
        Helpers.validate_string_start(data['token_id'], "tkn")
        
    def retrieve(self, id):
        Helpers.validate_string_start(id, "crd")
        
    def update(self, id):
        Helpers.validate_string_start(id, "crd")
        
    def list(self, data):
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