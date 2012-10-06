from django.test import TestCase
from pinry.api.tests.test_client import TestClient

class CommentPinTest(TestCase):
    def setUp(self):
        self.client = TestClient()

    def test_get_comments_for_pin(self):
        pass

    def test_comment_on_pin(self):
        pass


