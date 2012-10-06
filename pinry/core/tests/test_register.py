from django.utils import unittest
from django.test.client import Client
from django.core.urlresolvers import reverse

class TestRegister(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('core:register')

    def test_url(self):
        self.assertEqual(self.url, '/register/')

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_successful_registration(self):
        # If 302 was success, if 200 same page registration failed.
        response = self.client.post(self.url, {
            'username': 'test_registration_success',
            'password1': 'test_password',
            'password2': 'test_password',
        })
        self.assertEqual(response.status_code, 302)

    def test_failed_registration(self):
        # If 302 was success, if 200 same page registration failed.
        response = self.client.post(self.url, {
            'username': 'test_registration_failed',
            'password1': 'test_password',
            'password2': 'test_wrong_password',
        })
        self.assertEqual(response.status_code, 200)
