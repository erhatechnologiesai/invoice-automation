from fastapi import FastAPI
from app.config import settings
from app.models import InvoiceData
from app.services.invoice_parser import parse_and_validate_invoice

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.post("/process-invoice", response_model=InvoiceData)
def process_invoice(raw_payload: dict):
    text = raw_payload.get("raw_invoice_text", "")
    result = parse_and_validate_invoice(text)
    return InvoiceData(**result)
