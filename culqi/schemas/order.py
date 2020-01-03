SCHEMA = {
    "type": "object",
    "properties": {
        "amount":                   {"type" : "number"},
        "currency_code":            {"type" : "string"},
        "description":              {"type" : "string"},
        "order_number":             {"type" : "string"},
        "client_details":     {
            "type" : "object",
            "properties": {
                "first_name":       {"type" : "string"},
                "last_name":        {"type" : "string"},
                "email":            {"type" : "string"},
                "phone_number":     {"type" : "string"},
            }
        },
        "expiration_date":          {"type" : "number"},
        "confirm":                  {"type" : "boolean"},
        "metadata":                 {"type" : "object"},
    },
    "required": ["amount", "currency_code", "description", "order_number", "expiration_date", "client_details"]
}