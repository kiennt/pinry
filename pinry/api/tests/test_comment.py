from django.test import TestCase
from pinry.api.tests.test_client import TestClient
from pinry.pins.models import *

class CommentPinTest(TestCase):
    fixtures = ['user.json', 'member.json', 'pins.json']

    def setUp(self):
        self.client = TestClient()
        self.client = TestClient()
        self.user = User.objects.get(username='test')
        self.member = self.user.get_profile()
        self.client.login_user(self.user)

    def test_get_comments_for_pin(self):
        res = self.client.get('/api/pin/%s/comment/')
        self.assertEquals(200, res.status_code)

    def test_create_comment_on_pin(self):
        pass


