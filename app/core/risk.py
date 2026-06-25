def calculate_risk(intent: str, missing_fields: list):
    if intent == "access_request":
        return "medium"

    if len(missing_fields) >= 2:
        return "medium"

    return "low"