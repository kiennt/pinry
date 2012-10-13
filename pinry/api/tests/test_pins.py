import nose
import json

from pinry.api.tests.test_base import TestBaseAPI
from pinry.pins.models import Pin

class TestPins(TestBaseAPI):
    def test_modify_pin(self):
        """ Create new pin and modify it """
        pin = self.create_new_pin(self.member)
        res = self.client.put('/api/pin/%s/' % pin.pk, data=json.dumps({
                    "description" : "new test"
                }), content_type="application/json")
        pin = Pin.objects.get(pk=pin.pk)
        self.assertEquals("new test", pin.description)

    def test_modify_other_pin(self):
        """ Modify other pin """
        pin = Pin.objects.exclude(submitter=self.member)[0]
        description = pin.description
        res = self.client.put('/api/pin/%s/' % pin.pk, data=json.dumps({
                    "description" : "new test"
                }), content_type="application/json")
        pin = Pin.objects.get(pk=pin.pk)
        self.assertEquals(description, pin.description)

    def test_delete_pin(self):
        """ Create new pin and delete it. Check number of pin """
        pin_count = self.count_pins(self.member)
        pin = self.create_new_pin(self.member)
        self.assertEquals(pin_count + 1, self.count_pins(self.member))
        res = self.client.delete('/api/pin/%s/' % pin.pk)
        self.assertEquals(pin_count, self.count_pins(self.member))

    def test_delete_other_user_pin(self):
        """ Try to delete other pin """
        pin = Pin.objects.exclude(submitter=self.member)[0]

        pin_count = self.count_pins(self.member)
        res = self.client.delete('/api/pin/%s/' % pin.pk)
        self.assertEquals(pin_count, self.count_pins(self.member))

    def test_get_pin(self):
        """ Get a specific pin """
        pin = self.create_new_pin(self.member)
        res = self.client.get('/api/pin/%s/' % pin.pk)
        self.assertEquals(200, res.status_code)
        data = json.loads(res.content)
        self.assertEquals(pin.url, data['url'])
        self.assertEquals(self.user.username, data['author'])
        self.assertEquals(pin.image.url, data['image'])
        self.assertEquals(pin.thumbnail.url, data['thumbnail'])
        self.assertEquals([], data['tags'])

    def test_get_list_pins(self):
        """ Get list of pin """
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
