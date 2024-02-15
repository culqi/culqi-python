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
        
    def additional_validation(data, required_fields):
        for field in required_fields:
            if field not in data or data[field] is None or data[field] == "" or data[field] == "undefined":
                return ValueError(f"El campo '{field}' es requerido.")

        return None  
    
    def validate_initial_cycles_parameters(initial_cycles):
        parameters_initial_cycles = ['count', 'has_initial_charge', 'amount', 'interval_unit_time']
        for campo in parameters_initial_cycles:
            if campo not in initial_cycles:
                raise ValueError(f"El campo obligatorio '{campo}' no está presente en 'initial_cycles'.")
    
        if not isinstance(initial_cycles['count'], int):
            raise ValueError(f"El campo 'initial_cycles.count' es inválido o está vacío, debe tener un valor numérico.")
        
        if not isinstance(initial_cycles['has_initial_charge'], bool):
            raise ValueError(f"El campo 'initial_cycles.has_initial_charge' es inválido o está vacío. El valor debe ser un booleano (true o false).")
        
        if not isinstance(initial_cycles['amount'], int):
            raise ValueError(f"El campo 'initial_cycles.amount' es inválido o está vacío, debe tener un valor numérico.")

        valuesIntervalUnitTime = [1, 2, 3, 4, 5, 6]
        if not isinstance(initial_cycles['interval_unit_time'], int) or initial_cycles['interval_unit_time'] not in valuesIntervalUnitTime:
            raise ValueError(f"El campo 'initial_cycles.interval_unit_time' tiene un valor inválido o está vacío. Estos son los únicos valores permitidos: [1,2,3,4,5,6]")
        
    def validate_enum_currency(currency):
        allowed_values = ["PEN", "USD"]
        if currency in allowed_values:
            return None  # El valor está en la lista, no hay error

        # Si llega aquí, significa que el valor no está en la lista
        raise CustomException(f"El campo 'currency' es inválido o está vacío, el código de la moneda en tres letras (Formato ISO 4217). Culqi actualmente soporta las siguientes monedas: {allowed_values}.")


    def validate_currency(self, currency, amount):
        err = self.validate_enum_currency(currency)
        if err is not None:
            return CustomException(str(err))

        min_amount_pen = 3 * 100
        max_amount_pen = 5000 * 100
        min_amount_usd = 1 * 100
        max_amount_usd = 1500 * 100

        min_amount_public_api = min_amount_pen
        max_amount_public_api = max_amount_pen

        if currency == "USD":
            min_amount_public_api = min_amount_usd
            max_amount_public_api = max_amount_usd

        valid_amount = min_amount_public_api <= int(amount) <= max_amount_public_api

        if not valid_amount:
            return CustomException(f"El campo 'amount' admite valores en el rango {min_amount_public_api} a {max_amount_public_api}.")

        return None
    
    def validate_initial_cycles(self, has_initial_charge, currency, amount, pay_amount, count):
        if has_initial_charge:
            err = self.validate_currency(Helpers, currency, amount)
            if err is not None:
                return err

            if amount == pay_amount:
                raise CustomException("El campo 'initial_cycles.amount' es inválido o está vacío. El valor no debe ser igual al monto del plan.")

            if not (1 <= count <= 9999):
                raise CustomException("El campo 'initial_cycles.count' solo admite valores numéricos en el rango 1 a 9999.")

            if not (300 <= pay_amount <= 500000):
                raise CustomException("El campo 'initial_cycles.amount' solo admite valores numéricos en el rango 300 a 500000.")
        else:
            if not (0 <= count <= 9999):
                raise CustomException("El campo 'initial_cycles.count' solo admite valores numéricos en el rango 0 a 9999.")

            if pay_amount != 0:
                raise CustomException("El campo 'initial_cycles.amount' es inválido, debe ser 0.")

    def validate_image(image):
    # Expresión regular para validar URLs
        regex_image = r'^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-zA-Z0-9]+([-.]{1}[a-zA-Z0-9]+)*\.[a-zA-Z]{2,5}(:[0-9]{1,5})?(\/.*)?$'

        # Verificar si 'image' es una cadena y cumple con los criterios de validación
        if not (isinstance(image, str) and (5 <= len(image) <= 250) and re.match(regex_image, image)):
            # La imagen no cumple con los criterios de validación
            raise CustomException("El campo 'image' es inválido. Debe ser una cadena y una URL válida.")
    
    def validate_metadata(self, metadata):
        # Permitir un diccionario vacío para el campo metadata
        if not metadata:
            return None

        # Verificar límites de longitud de claves y valores
        error_length = self.validate_key_and_value_length(metadata)
        if error_length is not None:
            raise CustomException(error_length)

        # Convertir el diccionario transformado a JSON
        try:
            json.dumps(metadata)
        except json.JSONDecodeError as e:
            return e

        return None

    def validate_key_and_value_length(obj_metadata):
        max_key_length = 30
        max_value_length = 200

        for key, value in obj_metadata.items():
            key_str = str(key)
            value_str = str(value)
            # Verificar límites de longitud de claves
            if not (1 <= len(key_str) <= max_key_length) or not (1 <= len(value_str) <= max_value_length):
                return f"El objeto 'metadata' es inválido, límite key (1 - {max_key_length}), value (1 - {max_value_length})."

        return None 
