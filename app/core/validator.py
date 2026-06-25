def validate_entities(entities: dict):
    missing = []

    if not entities["name"]:
        missing.append("name")

    if not entities["vehicle"]:
        missing.append("vehicle")

    return missing