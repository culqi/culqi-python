class Data(object):
    CARD = {
        "successful": {
            "visa": {
                "card_number": "4111111111111111",
                "expiration_month": "09",
                "expiration_year": "2025",
                "cvv": "123",
                "email": "richard@piedpiper.com",
            },
            "master_card": {
                "card_number": "5111111111111118",
                "expiration_month": "06",
                "expiration_year": "2025",
                "cvv": "039",
                "email": "richard@piedpiper.com",
            },
            "american_express": {
                "card_number": "371212121212122",
                "expiration_month": "11",
                "expiration_year": "2025",
                "cvv": "2841",
                "email": "richard@piedpiper.com",
            },
            "diners_club": {
                "card_number": "36001212121210",
                "expiration_month": "04",
                "expiration_year": "2025",
                "cvv": "964",
                "email": "richard@piedpiper.com",
            },
        },
        "stolen_card": {
            "visa": {
                "card_number": "4000020000000000",
                "expiration_month": "10",
                "expiration_year": "2025",
                "cvv": "354",
                "email": "richard@piedpiper.com",
            }
        },
        "lost_card": {
            "visa": {
                "card_number": "4000030000000009",
                "expiration_month": "08",
                "expiration_year": "2025",
                "cvv": "836",
                "email": "richard@piedpiper.com",
            }
        },
        "insufficient_funds": {
            "visa": {
                "card_number": "4000040000000008",
                "expiration_month": "03",
                "expiration_year": "2025",
                "cvv": "295",
                "email": "richard@piedpiper.com",
            }
        },
        "contact_issuer": {
            "master_card": {
                "card_number": "5400000000000005",
                "expiration_month": "01",
                "expiration_year": "2025",
                "cvv": "492",
                "email": "richard@piedpiper.com",
            }
        },
        "incorrect_cvv": {
            "master_card": {
                "card_number": "5400020000000003",
                "expiration_month": "07",
                "expiration_year": "2025",
                "cvv": "203",
                "email": "richard@piedpiper.com",
            }
        },
        "issuer_not_available": {
            "american_express": {
                "card_number": "370001000000000",
                "expiration_month": "04",
                "expiration_year": "2025",
                "cvv": "2511",
                "email": "richard@piedpiper.com",
            }
        },
        "issuer_decline_operation": {
            "american_express": {
                "card_number": "370002000000008",
                "expiration_month": "05",
                "expiration_year": "2025",
                "cvv": "1810",
                "email": "richard@piedpiper.com",
            }
        },
        "invalid_card": {
            "diners_club": {
                "card_number": "36000000000008",
                "expiration_month": "09",
                "expiration_year": "2025",
                "cvv": "683",
                "email": "richard@piedpiper.com",
            }
        },
        "processing_error": {
            "diners_club": {
                "card_number": "36000100000007",
                "expiration_month": "12",
                "expiration_year": "2025",
                "cvv": "820",
                "email": "richard@piedpiper.com",
            }
        },
        "fraudulent": {
            "diners_club": {
                "card_number": "36000200000006",
                "expiration_month": "01",
                "expiration_year": "2025",
                "cvv": "230",
                "email": "richard@piedpiper.com",
            }
        },
    }

    CARD["successful"]["visa"] = {
        "brand": "Visa",
        "card_number": "4111111111111111",
        "expiration_month": "09",
        "expiration_year": "2025",
        "cvv": "123",
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
