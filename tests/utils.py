class Data:
    TOKEN = {
        "cvv": "123",
        "card_number": "4111111111111111",
        "expiration_year": "2020",
        "expiration_month": "09",
        "email": "richard@piedpiper.com",
    }

    CHARGE = {
        "amount": "10000",
        "capture": False,
        "currency_code": "PEN",
        "description": "Venta de prueba",
        "email": "richard@piedpiper.com",
        "installments": 0,
        "source_id": None
    }

    REFUND = {
        "amount": 100,
        "reason": "solicitud_comprador",
        "charge_id": None,
    }

    CUSTOMER = {
        "address": "Avenida Lima 123213",
        "address_city": "LIMA",
        "country_code": "PE",
        "email": None,
        "first_name": "Richard",
        "last_name": "Piedpiper",
        "phone_number": "+51998989789",
    }
