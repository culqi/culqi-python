import re
import json
import datetime
from culqi.utils.validation.country_codes import get_country_codes
from culqi.utils.errors import CustomException
from culqi.utils.validation.helpers import Helpers

class SubscriptionValidation:
        
    def create(self, data):
        requerid_payload = ['card_id', 'plan_id', 'tyc']
        resultValidation = Helpers.additional_validation(data, requerid_payload)
        if resultValidation is not None:
            raise CustomException(f"{resultValidation}")
        else:
            # Validate card_id
            if not isinstance(data['card_id'], str) or len(data['card_id'])!= 25:
                raise CustomException("El campo 'card_id' es inválido. La longitud debe ser de 25.")
            Helpers.validate_string_start(data['card_id'], "crd")

            # Validate plan_id
            if not isinstance(data['plan_id'], str) or len(data['plan_id'])!= 25:
                raise CustomException("El campo 'plan_id' es inválido. La longitud debe ser de 25.")            
            Helpers.validate_string_start(data['plan_id'], "pln")

            # Validate tyc
            if not isinstance(data['tyc'], bool) :
                raise CustomException("El campo 'tyc' es inválido o está vacío. El valor debe ser un booleano.")

            # Validate metadata
            if 'metadata' in data:
                Helpers.validate_metadata(Helpers, data['metadata'])

            
        
    def retrieve(self, id):
        Helpers.validate_string_start(id, "sxn")
        if len(id) != 25:
            raise CustomException("El campo 'id' es inválido. La longitud debe ser de 25 caracteres.")
        
        
    def update(self, id, data):
        Helpers.validate_string_start(id, "sxn")
        if len(id) != 25:
            raise CustomException("El campo 'id' es inválido. La longitud debe ser de 25 caracteres.")
        # Validate data update
        requerid_payload = ['card_id']
        resultValidation = Helpers.additional_validation(data, requerid_payload)
        if resultValidation is not None:
            raise CustomException(f"{resultValidation}")
        else:
            # Validate card_id
            if not isinstance(data['card_id'], str) or len(data['card_id'])!= 25:
                raise CustomException("El campo 'card_id' es inválido. La longitud debe ser de 25.")
            Helpers.validate_string_start(data['card_id'], "crd")

            # Validate metadata
            if 'metadata' in data:
                Helpers.validate_metadata(Helpers, data['metadata'])
        
    def list(self, data):
        # Validate parameters status
        
        # Validate plan_id
        if 'plan_id' in data:
            if not isinstance(data['plan_id'], str) or len(data['plan_id'])!= 25:
                raise CustomException("El campo 'plan_id' es inválido. La longitud debe ser de 25.")
            Helpers.validate_string_start(data['plan_id'], "pln")
            
        if 'status' in data:
            valuesStatus = [1, 2, 3, 4, 5, 6, 8]
            if not isinstance(data['status'], int) or data['status'] not in valuesStatus:
                raise CustomException("El campo 'status' es inválido. Estos son los únicos valores permitidos: 1, 2, 3, 4, 5, 6, 8")
        
        # Validate parameters creation_date_from          
        if 'creation_date_from' in data :
            if not isinstance(data['creation_date_from'], str) or  not(len(data['creation_date_from']) == 10 or len(data['creation_date_from']) == 13) :
                raise CustomException("El campo 'creation_date_from' debe tener una longitud de 10 o 13 caracteres.")

        # Validate parameters creation_date_to
        if 'creation_date_to' in data :
            if not isinstance(data['creation_date_to'], str) or  not(len(data['creation_date_to']) == 10 or len(data['creation_date_to']) == 13) :
                raise CustomException("El campo 'creation_date_to' debe tener una longitud de 10 o 13 caracteres.")
        
        # Validate parameters before
        if 'before' in data :
            if not isinstance(data['before'], str) or len(data['before']) != 25  :
                raise CustomException("El campo 'before' es inválido. La longitud debe ser de 25 caracteres")
            
        # Validate parameters after
        if 'after' in data :
            if not isinstance(data['after'], str) or len(data['after']) != 25  :
                raise CustomException("El campo 'after' es inválido. La longitud debe ser de 25 caracteres")

        # Validate parameters limit
        if 'limit' in data :
            rangeLimit = range(1, 101)
            if not isinstance(data['limit'], int) or data['limit'] not in rangeLimit:
                raise CustomException("El filtro 'limit' admite valores en el rango 1 a 100")
        
        if 'creation_date_from' in data and 'creation_date_to' in data:
            Helpers.validate_date_filter(data['creation_date_from'], data['creation_date_to'])
        