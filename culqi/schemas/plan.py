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
    "required": ["name", "amount", "currency_code", "interval", "interval_count"]
}