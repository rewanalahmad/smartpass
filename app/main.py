from fastapi import FastAPI
from pydantic import BaseModel
import json
from fastapi.middleware.cors import CORSMiddleware

from app.core.intent import detect_intent
from app.core.extractor import extract_entities
from app.core.validator import validate_entities
from app.core.risk import calculate_risk

app = FastAPI(title="SmartPass AI Validator")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputText(BaseModel):
    text: str


@app.get("/")
def root():
    return {"message": "SmartPass AI is running"}


@app.post("/validate")
def validate(data: InputText):
    text = data.text

    intent = detect_intent(text)
    entities = extract_entities(text)
    missing = validate_entities(entities)
    risk = calculate_risk(intent, missing)

    return {
        "intent": intent,
        "extracted_data": entities,
        "missing_fields": missing,
        "risk_level": risk,
        "valid": len(missing) == 0
    }