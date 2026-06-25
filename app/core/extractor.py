import re

def extract_entities(text: str):
    text_lower = text.lower()

    name_match = re.search(r"my name is (\w+)", text_lower)
    name = name_match.group(1) if name_match else None

    vehicles = ["bmw", "audi", "mercedes", "toyota", "tesla"]
    vehicle = next((v for v in vehicles if v in text_lower), None)

    date_keywords = ["today", "tomorrow", "next week", "friday", "monday"]
    date = next((d for d in date_keywords if d in text_lower), None)

    return {
        "name": name,
        "vehicle": vehicle,
        "date": date
    }