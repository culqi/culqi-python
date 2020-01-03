SCHEMA = {
    "type": "object",
    "properties": {
        "card_id":      {"type" : "string"},
        "plan_id":      {"type" : "string"},
        "metadata":     {"type" : "object"}
    },
    "required": ["card_id", "plan_id"]
}