SCHEMA = {
    "type": "object",
    "properties": {
        "customer_id":  {"type" : "string"},
        "token_id":     {"type" : "string"},
        "validate":     {"type" : "boolean"},
        "metadata":     {"type" : "object"}
    },
    "required": ["customer_id", "token_id"]
}