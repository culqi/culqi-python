import re
import json
import datetime
from culqi.utils.validation.country_codes import get_country_codes
from culqi.utils.errors import CustomException
from culqi.utils.validation.helpers import Helpers

class RefundValidation:
        
    def create(self, data):
        # Validate charge format
        Helpers.validate_string_start(data['charge_id'], "chr")

        # Validate reason
        allowed_values = ['duplicado', 'fraudulento', 'solicitud_comprador']
        Helpers.validate_value(data['reason'], allowed_values)

        # Validate amount
        if not isinstance(data['amount'], (int, float)) or int(data['amount']) != data['amount']:
            raise CustomException('Invalid amount.')
        
    def retrieve(self, id):
        Helpers.validate_string_start(id, "ref")
        
    def update(self, id):
        Helpers.validate_string_start(id, "ref")
        
    def list(self, data):
        # Validate reason
        if 'reason' in data:
            allowed_values = ['duplicado', 'fraudulento', 'solicitud_comprador']
            Helpers.validate_value(data['reason'], allowed_values)
            
        if 'creation_date_from' in data and 'creation_date_to' in data:
            Helpers.validate_date_filter(data['creation_date_from'], data['creation_date_to'])