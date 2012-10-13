from django.test import TestCase
from django.contrib.auth.models import User

from pinry.api.tests.test_client import TestClient
from pinry.pins.models import *

class TestBaseAPI(TestCase):
    fixtures = ['user.json', 'member.json', 'pins.json']

    def setUp(self):
        self.client = TestClient()
        self.user = User.objects.get(username='test')
        self.member = self.user.get_profile()
        self.client.login_user(self.user)

    def count_pins(self, member):
        return Pin.objects.filter(submitter=member).count()

    def create_new_pin(self, member):
        return Pin.objects.create(
                submitter=member,
                url='',
                image='test.jpg',
                thumbnail='test_thumb.jpg')
