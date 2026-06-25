import re

def detect_intent(text: str) -> str:
    text = text.lower()

    if "service" in text or "repair" in text or "fix" in text:
        return "service_booking"

    if "buy" in text or "purchase" in text or "price" in text:
        return "sales_inquiry"

    if "access" in text or "login" in text or "permission" in text:
        return "access_request"

    return "general_inquiry"

def extract_entities(text: str):
    text_lower = text.lower()

    # simple name detection (very basic for demo)
    name_match = re.search(r"my name is (\w+)", text_lower)
    name = name_match.group(1) if name_match else None

    # vehicle detection
    vehicles = ["bmw", "audi", "mercedes", "toyota", "tesla"]
    vehicle = next((v for v in vehicles if v in text_lower), None)

    # date detection (very simple)
    date_keywords = ["today", "tomorrow", "next week", "friday", "monday"]
    date = next((d for d in date_keywords if d in text_lower), None)

    return {
        "name": name,
        "vehicle": vehicle,
        "date": date
    }

def validate_input(entities: dict):
    missing = []

    if not entities["name"]:
        missing.append("name")

    if not entities["vehicle"]:
        missing.append("vehicle")

    return missing