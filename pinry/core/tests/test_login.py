from django.utils import unittest
from django.test.client import Client
from django.core.urlresolvers import reverse


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('core:login')

    def test_url(self):
        self.assertEqual(self.url, '/login/')

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
