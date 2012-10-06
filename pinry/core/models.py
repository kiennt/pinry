from django.db import models
from django.contrib.auth.models import User
from social_auth.db.django_models import UserSocialAuth
from social_auth.signals import socialauth_registered

class Member(models.Model):
    user = models.OneToOneField(User, null=True)

    def __unicode__(self):
        return self.user.username

def new_users_handler(sender, user, response, details, **kwargs):
    user.is_new = True
    Member.objects.create(user=user)
    return False

socialauth_registered.connect(new_users_handler, sender=None)
