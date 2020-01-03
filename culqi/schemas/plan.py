SCHEMA = {
    "type": "object",
    "properties": {
        "name":             {"type" : "string"},
        "amount":           {"type" : "number"},
        "currency_code":    {"type" : "string"},
        "interval":         {"type" : "string"},
        "interval_count":   {"type" : "number"},
        "trial_days":       {"type" : "number"},
        "limit":            {"type" : "number"},
        "metadata":         {"type" : "object"}
    },
    "required": ["first_name", "last_name", "email", "address", "address_city", "country_code", "phone_number"]
}