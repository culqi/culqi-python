import time

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
        "short_name": "cppe4",
        "description": "Cypress PCI  ERRROR NO USAR",
        "amount": 300,
        "currency": "PEN",
        "interval_unit_time": 1,
        "interval_count": 1,
        "initial_cycles": {
          "count": 1,
          "has_initial_charge": False,
          "amount": 0,
          "interval_unit_time": 1
        },
        "name": None,
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
        "expiration_date": int(time.time()) + 3600,
        "confirm": False,
    }
