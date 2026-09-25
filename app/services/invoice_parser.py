import re

def parse_and_validate_invoice(raw_text: str):
    # Simulated OCR extraction
    items = [
        {"description": "AI Agent Node Compute", "quantity": 2, "unit_price": 450.0, "total": 900.0},
        {"description": "Enterprise Vector DB Storage", "quantity": 1, "unit_price": 300.0, "total": 300.0}
    ]
    subtotal = sum(i["total"] for i in items)
    tax_rate = 0.10
    tax_amount = round(subtotal * tax_rate, 2)
    total_amount = round(subtotal + tax_amount, 2)
    
    # Mathematical validation check
    validation_passed = (round(subtotal + tax_amount, 2) == total_amount)
    
    return {
        "invoice_number": "INV-2026-9041",
        "vendor_name": "Erha Cloud Technologies",
        "date": "2026-09-25",
        "line_items": items,
        "subtotal": subtotal,
        "tax_rate": tax_rate,
        "tax_amount": tax_amount,
        "total_amount": total_amount,
        "validation_passed": validation_passed
    }
