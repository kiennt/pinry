import nose
import json
from django.test import TestCase
from django.contrib.auth.models import User

from pinry.api.tests.test_client import TestClient
from pinry.pins.models import Pin

class TestPins(TestCase):
    fixtures = ['user.json', 'member.json', 'pins.json']

    def setUp(self):
        self.client = TestClient()
        self.user = User.objects.get(username='test')
        self.member = self.user.get_profile()
        self.client.login_user(self.user)

    def _count_pins(self, member):
        return Pin.objects.filter(submitter=member).count()

    def _create_new_pin(self, member):
        return Pin.objects.create(
                submitter=member,
                url='',
                image='test.jpg',
                thumbnail='test_thumb.jpg')

    def test_create_pin(self):
        pin_count = self._count_pins(self.member)

        with open('media/pins/pin/originals/1135968047.jpg') as f:
            res = self.client.post('/api/pin/', {
                        'url': '',
                        'image': f.read(),
                        'description': 'testing api create pin',
                        'tags': ['girls']
                    })
            self.assertEquals(200, res.status_code)
            self.assertEquals(pin_count + 1, self._count_pins(self.member))

    def test_delete_pin(self):
        pin_count = self._count_pins(self.member)
        pin = self._create_new_pin(self.member)
        res = self.client.delete('/api/pin/%s/' % pin.pk)
        self.assertEquals(200, res.status_code)
        self.assertEquals(pin_count, self._count_pins(self.member))

    def test_get_pin(self):
        pin = self._create_new_pin(self.member)
        res = self.client.get('/api/pin/%s/' % pin.pk)
        self.assertEquals(200, res.status_code)
        data = json.loads(res.content)
        self.assertEquals(pin.pk, data['pk'])
        self.assertEquals(pin.url, data['url'])
        self.assertEquals(pin.submitter.pk, data['submitter'])
        self.assertEquals(pin.image, data['image'])
        self.assertEquals(pin.thumbnail, data['thumbnail'])
        self.assertEquals(pin.tags, data['tags'])

    def test_get_list_pins(self):
        res = self.client.get('/api/pin/?limit=5')
        self.assertEquals(200, res.status_code)
        data = json.loads(res.content)
        objects = data['objects']
        self.assertEquals(5, len(objects))
        for pin in objects:
            pin_keys = ["author", "description", "id", "url", "image",
                        "thumbnail", "is_owner", "published",
                        "repin", "tags", "view_count"]
            self.assertEquals(sorted(pin_keys), sorted(pin.keys()))
