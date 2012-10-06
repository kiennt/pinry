from social_auth.signals import socialauth_registered

def new_users_handler(sender, user, response, details, **kwargs):
    user.is_new = True
    if user.is_new:
        avatar = urlopen(url)
        profile = UserProfile(user=user)

    return False

socialauth_registered.connect(new_users_handler, sender=None)
