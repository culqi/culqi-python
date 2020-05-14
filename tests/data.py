class Data:
    TOKEN = {
        "cvv": "123",
        "card_number": "4111111111111111",
        "expiration_year": "2025",
        "expiration_month": "09",
        "email": "richard@piedpiper.com",
    }

    CHARGE = {
        "amount": 1000,
        "capture": False,
        "currency_code": "PEN",
        "description": "Venta de prueba",
        "email": "richard@piedpiper.com",
        "installments": 0,
        "source_id": None,
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

    PLAN = {
        "amount": 1000,
        "currency_code": "PEN",
        "interval": "dias",
        "interval_count": 2,
        "limit": 10,
        "name": None,
        "trial_days": 30,
    }

    ORDER = {
        "amount": 1000,
        "currency_code": "PEN",
        "description": "Venta de prueba",
        "order_number": None,
        "client_details": {
            "first_name": "Richard",
            "last_name": "Piedpiper",
            "email": "richard@piedpiper.com",
            "phone_number": "+51998989789",
        },
        "expiration_date": 1893474000,
        "confirm": False,
    }
