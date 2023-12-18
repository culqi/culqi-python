import re
import json
import datetime
from culqi.utils.validation.country_codes import get_country_codes
from culqi.utils.errors import CustomException
from culqi.utils.validation.helpers import Helpers

class SubscriptionValidation:
        
    def create(self, data):
        # Validate card and plan format
        Helpers.validate_string_start(data['card_id'], "crd")
        Helpers.validate_string_start(data['plan_id'], "pln")
        
    def retrieve(self, id):
        Helpers.validate_string_start(id, "sxn")
        
    def update(self, id):
        Helpers.validate_string_start(id, "sxn")
        
    def list(self, data):
        if 'plan_id' in data:
            Helpers.validate_string_start(data['plan_id'], "pln")
        
        if 'creation_date_from' in data and 'creation_date_to' in data:
            Helpers.validate_date_filter(data['creation_date_from'], data['creation_date_to'])
        