from django.db import models
from django.contrib.auth.models import User
from social_auth.db.django_models import UserSocialAuth

class Member(models.Model):
    user = models.ForeignKey(User, null=True)
    social_user = models.ForeignKey(UserSocialAuth, null=True)

    def __unicode__(self):
        return self.user.username

    @property
    def facebook_access_token(self):
        if not hasattr(self, '_fb_access_token'):
            try:
                info = self.social_user.get(provider='facebook')
                self._fb_access_token = info.extra_data['access_token']
            except:
                self._fb_access_token = None
        return self._fb_access_token
