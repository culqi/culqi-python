SCHEMA = {
    "type": "object",
    "properties": {
        "amount":               {"type" : "number"},
        "capture":              {"type" : "boolean"},
        "installments":         {"type" : "number"},
        "currency_code":        {"type" : "string"},
        "email":                {"type" : "string"},
        "description":          {"type" : "string"},
        "source_id":            {"type" : "string"},
        "metadata":             {"type" : "object"},
        "antifraud_details":     {
            "type": "object",
            "properties": {
                "address":      {"type" : "string"},
                "address_city": {"type" : "string"},
                "country_code": {"type" : "string"},
                "first_name":   {"type" : "string"},
                "last_name":    {"type" : "string"},
                "phone_number": {"type" : "number"},
            },
        },
    },
    "required": ["amount", "currency_code", "email", "source_id"]
}