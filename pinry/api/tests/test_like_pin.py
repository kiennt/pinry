from django.test import TestCase
from pinry.api.tests.test_client import TestClient

class LikePinTest(TestCase):
    fixtures = ['user.json', 'social_auth.json', 'member.json', 'pin.json']

    def setUp(self):
        self.client = TestClient()

    def test_get_likes_for_pin(self):
        pass

    def test_like_pin(self):
        pass
