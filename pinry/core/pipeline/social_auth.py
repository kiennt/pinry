from django.contrib.auth.models import User
from pinry.core.models import Member

def create_member(backend, details, response, user, is_new, *args, **kwargs):
    if is_new and user:
        member = Member.objects.create(user=user,
                social_user=kwargs['social_user'])
        return member
    return None
