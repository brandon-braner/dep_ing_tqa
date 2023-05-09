import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestPayments(unittest.TestCase):
    def test_get_payment(self):
        response = client.get("/payments")
        self.assertEqual(response.status_code, 200)