from django.utils import unittest
from django.test.client import Client
from django.core.urlresolvers import reverse

class TestLogout(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('core:logout')
        self.client.post(self.url, {
            'username': 'test_user_logout',
            'password1': 'test_password',
            'password2': 'test_password',
        })

    def test_url(self):
        self.assertEqual(self.url, '/logout/')

    def test_logout_with_logged_in_user(self):
        self.client.post(self.url, {
            'username': 'test_user_logout',
            'password': 'test_password'
        })
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
