from django.test import TestCase
from pinry.api.tests.test_client import TestClient

class TestRecentPins(TestCase):
    def setUp(self):
        self.client = TestClient()
        self.url = '/api/pin/?format=json'

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_delete_pin(self):
        pass

    def test_get_list_pins(self):
        pass

    def test_get_pin(self):
        pass

