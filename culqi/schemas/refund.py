SCHEMA = {
    "type": "object",
    "properties": {
        "amount":           {"type" : "number"},
        "charge_id":        {"type" : "string"},
        "reason":           {"type" : "string"},
    },
    "required": ["amount", "charge_id", "reason"]
}