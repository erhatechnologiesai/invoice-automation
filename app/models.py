from pydantic import BaseModel
from typing import List, Optional

class InvoiceItem(BaseModel):
    description: str
    quantity: int
    unit_price: float
    total: float

class InvoiceData(BaseModel):
    invoice_number: str
    vendor_name: str
    date: str
    line_items: List[InvoiceItem]
    subtotal: float
    tax_rate: float
    tax_amount: float
    total_amount: float
    validation_passed: bool
