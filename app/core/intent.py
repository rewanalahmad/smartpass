def detect_intent(text: str) -> str:
    text = text.lower()

    if "service" in text or "repair" in text or "fix" in text:
        return "service_booking"

    if "buy" in text or "purchase" in text or "price" in text:
        return "sales_inquiry"

    if "access" in text or "login" in text or "permission" in text:
        return "access_request"

    return "general_inquiry"