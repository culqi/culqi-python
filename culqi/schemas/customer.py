SCHEMA = {
    "type": "object",
    "properties": {
        "first_name":       {"type" : "string"},
        "last_name":        {"type" : "string"},
        "email":            {"type" : "string"},
        "address":          {"type" : "string"},
        "address_city":     {"type" : "string"},
        "country_code":     {"type" : "string"},
        "phone_number":     {"type" : "string"},
        "metadata":         {"type" : "object"}
    },
    "required": ["first_name", "last_name", "email", "address", "address_city", "country_code", "phone_number"]
}