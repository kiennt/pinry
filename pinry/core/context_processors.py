from django.conf import settings


def template_settings(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
    return {
        'site_name': settings.SITE_NAME,
        'API_LIMIT_PER_PAGE': settings.API_LIMIT_PER_PAGE,
        'username': username
    }
