class Data:
    TOKEN = {
        "cvv": "123",
        "card_number": "4111111111111111",
        "expiration_year": "2025",
        "expiration_month": "09",
        "email": "richard@piedpiper.com",
    }

    YAPE = {
        "amount": "36200",
        "fingerprint": "86d3c875769bf62b0471b47853bfda77",
        "number_phone": "900000001",
        "otp": "425251",
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
        "email": "usuario@culqi.com",
        "first_name": "Richard",
        "last_name": "Piedpiper",
        "phone_number": "998989789",
    }

    PLAN = {
        "short_name": "cp-prueb2442",
        "description": "Cypress PCI | ERRROR NO USAR",
        "amount": 300,
        "currency": "PEN",
        "interval_unit_time": 1,
        "interval_count": 1,
        "initial_cycles": {
          "count": 1,
          "has_initial_charge": True,
          "amount": 400,
          "interval_unit_time": 1
        },
        "name": None,
        "image": "https://recurrencia-suscripciones-qa.s3.amazonaws.com/f097e1d5-e365-42f3-bc40-a27beab80f54",
	    "metadata":{}
    }

    ORDER = {
        "amount": 1000,
        "currency_code": "PEN",
        "description": "Venta de prueba",
        "order_number": '12346shsbs_skd',
        "client_details": {
            "first_name": "Richard",
            "last_name": "Piedpiper",
            "email": "richard@piedpiper.com",
            "phone_number": "+51998989789",
        },
        "expiration_date": 1893474000,
        "confirm": False,
    }
