import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestInvoiceAutomation(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_invoice_validation(self):
        res = self.client.post("/process-invoice", json={"raw_invoice_text": "Invoice #INV-2026-9041 Total: $1320"})
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertTrue(data["validation_passed"])
        self.assertEqual(data["total_amount"], 1320.0)

if __name__ == "__main__":
    unittest.main()
