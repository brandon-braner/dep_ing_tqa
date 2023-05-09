import unittest
from fastapi.testclient import TestClient
from main import app
from unittest.mock import Mock, patch

client = TestClient(app)


class TestPayments(unittest.TestCase):
    def test_get_payment(self):
        response = client.get("/payments")
        resp_json = response.json()

        assert resp_json == {'payments': [[123, 321, 1]]}

    @patch("app.modules.payments.routes.get_db_conn")
    def test_get_payment_mock(self, mock_get_db_conn):

        expected_result = [[123123123, 1321, 10]]
        mock_cursor = Mock()
        mock_cursor.execute.return_value = None
        mock_cursor.fetchall.return_value = expected_result
        mock_get_db_conn.return_value = [None, mock_cursor]
        mock_get_db_conn.execute.return_value = None
        response = client.get("/payments")
        resp_json = response.json()

        assert resp_json == {'payments': expected_result}



    @patch("app.modules.payments.utils.get_db_conn")
    def test_get_payment_mock(self, mock_get_db_conn):
        # had to patch the utils since we are getting this from a file not the container.
        # A true di container would do this for us
        expected_result = [[123123123, 1321, 10]]
        mock_cursor = Mock()
        mock_cursor.execute.return_value = None
        mock_cursor.fetchall.return_value = expected_result
        mock_get_db_conn.return_value = [None, mock_cursor]
        mock_get_db_conn.execute.return_value = None
        response = client.get("/payments")
        resp_json = response.json()

        assert resp_json == {'payments': expected_result}