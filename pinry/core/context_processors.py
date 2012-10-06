from django.conf import settings


def template_settings(request):
    return {
        'site_name': settings.SITE_NAME,
        'FACEBOOK_APP_ID' : settings.FACEBOOK_APP_ID,
    }
