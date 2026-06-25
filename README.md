# SmartPass AI Validator

SmartPass AI is a lightweight full-stack system that analyzes user requests and extracts structured intent and data.

It is designed to simulate real-world AI backend systems used in automation, validation, and workflow intelligence.

---

## 🚀 Features

- Accepts natural language input (e.g. service requests)
- Extracts structured data (name, intent, date, etc.)
- Returns clean JSON response
- FastAPI backend
- Simple frontend UI (HTML + JS)
- Ready for AI integration (LLM-ready architecture)

---

## 🧠 Example Input

## 📤 Example Output
My name is Alex and I want BMW service next Friday
```json
{
  "intent": "service_booking",
  "extracted_data": {
    "name": "alex",
    "vehicle": "bmw",
    "date": "friday"
  },
  "missing_fields": [],
  "risk_level": "low",
  "valid": true
}