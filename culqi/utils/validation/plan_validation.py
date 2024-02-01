import re
import json
import datetime
from culqi.utils.validation.country_codes import get_country_codes
from culqi.utils.errors import CustomException
from culqi.utils.validation.helpers import Helpers

class PlanValidation:
        
    def create(self, data):
        requerid_payload = ['short_name', 'description', 'amount', 'currency', 'interval_unit_time',
		'interval_count', 'initial_cycles', 'name']
        resultValidation = Helpers.additional_validation(data, requerid_payload)
        if resultValidation is not None:
            raise CustomException(f"{resultValidation}")
        else:

            # Validate interval_unit_time
            valuesIntervalUnitTime = [1, 2, 3, 4, 5, 6]
            if not isinstance(data['interval_unit_time'], int) or data['interval_unit_time'] not in valuesIntervalUnitTime:
                raise CustomException("El campo 'interval_unit_time' tiene un valor inválido o está vacío. Estos son los únicos valores permitidos: [ 1, 2, 3, 4, 5, 6]")

            # Validate interval_count
            rangeIntervalCount = range(0, 10000)
            if not isinstance(data['interval_count'], int) or data['interval_count'] not in rangeIntervalCount:
                raise CustomException("El campo 'interval_count' solo admite valores numéricos en el rango 0 a 9999.")
            
            #Validate amount
            if not isinstance(data['amount'], int):
                raise CustomException("El campo 'amount' es inválido o está vacío, debe tener un valor numérico.")

            #validateCurrency
            Helpers.validate_currency(Helpers, data['currency'], data['amount'])
            
            # Validate name
            rangeName = range(5, 51)
            if not isinstance(data['name'], str) or len(data['name']) not in rangeName:
                raise CustomException("El campo 'name' es inválido o está vacío. El valor debe tener un rango de 5 a 50 caracteres.")
        
            # Validate description
            rangeDescription = range(5, 251)
            if not isinstance(data['description'], str) or len(data['description']) not in rangeDescription:
                raise CustomException("El campo 'description' es inválido o está vacío. El valor debe tener un rango de 5 a 250 caracteres.")

            # Validate short_name
            rangeShortName = range(5,51)
            if not isinstance(data['short_name'], str) or len(data['name']) not in rangeShortName:
                raise CustomException("El campo'short_name' es inválido o está vacío. El valor debe tener un rango de 5 a 50 caracteres.")
            
            # Validate initial_cycles
            Helpers.validate_initial_cycles_parameters(data['initial_cycles'])
            initial_cycles = data['initial_cycles']
            Helpers.validate_initial_cycles(Helpers, initial_cycles['has_initial_charge'], data['currency'], data['amount'], initial_cycles['amount'], initial_cycles['count'])

            # Validate image
            if 'image' in data:
                Helpers.validate_image(data['image'])

            # Validate metadata
            if 'metadata' in data:
                Helpers.validate_metadata(Helpers, data['metadata'])
        
    def retrieve(self, id):
        Helpers.validate_string_start(id, 'pln')
        if len(id) != 25:
            raise CustomException("El campo 'id' es inválido. La longitud debe ser de 25 caracteres.")
        
    def update(self, id, data):
        Helpers.validate_string_start(id, 'pln')
        if len(id) != 25:
            raise CustomException("El campo 'id' es inválido. La longitud debe ser de 25 caracteres.")

        # Validate data update
        if 'short_name' in data:
            rangeShortName = range(5, 51)
            if not isinstance(data['short_name'], str) or len(data['short_name']) not in rangeShortName:
                raise CustomException("El campo 'short_name' es inválido o está vacío. El valor debe tener un rango de 5 a 50 caracteres.")
        
        if 'name' in data:
            rangeName = range(5, 51)
            if not isinstance(data['name'], str) or len(data['name']) not in rangeName:
                raise CustomException("El campo 'name' es inválido o está vacío. El valor debe tener un rango de 5 a 50 caracteres.")
        
        if 'description' in data:
            rangeDescription = range(5, 251)
            if not isinstance(data['description'], str) or len(data['description']) not in rangeDescription:
                raise CustomException("El campo 'description' es inválido o está vacío. El valor debe tener un rango de 5 a 250 caracteres.")
        
        # Validate image
        if 'image' in data:
            Helpers.validate_image(data['image'])
        
        # Validate metadata
        if 'metadata' in data:
                Helpers.validate_metadata(Helpers, data['metadata'])

        if 'status' in data:
            valuesStatus = [1, 2]
            if not isinstance(data['status'], int) or data['status'] not in valuesStatus:
                raise CustomException("El campo 'status' tiene un valor inválido o está vacío. Estos son los únicos valores permitidos: [ 1, 2 ]")

    def list(self, data):

        # Validate parameters status
        if 'status' in data:
            valuesStatus = [1, 2]
            if not isinstance(data['status'], int) or data['status'] not in valuesStatus:
                raise CustomException("El filtro 'status' tiene un valor inválido o está vacío. Estos son los únicos valores permitidos: 1, 2.")
        
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

        # Validate parameters max_amount
        if 'max_amount' in data :
            rangeMaxAmount = range(300, 500001)
            if not isinstance(data['max_amount'], int) or data['max_amount'] not in rangeMaxAmount:
                raise CustomException("El filtro 'max_amount' admite valores en el rango 300 a 500000")
            
        if 'min_amount' in data :
            rangeMinAmount = range(300, 500001)
            if not isinstance(data['min_amount'], int) or data['min_amount'] not in rangeMinAmount:
                raise CustomException("El filtro'min_amount' admite valores en el rango 300 a 500000")
            
        if 'creation_date_from' in data and 'creation_date_to' in data:
            Helpers.validate_date_filter(data['creation_date_from'], data['creation_date_to'])