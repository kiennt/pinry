from django.template import loader, Context, Library
from django.conf import settings

register = Library()

@register.simple_tag
def facebook_login(field):
    template = loader.get_template('core/templatetags/facebook_login.html')
    return template.render(Context({
                'FB_APP_ID' : settings.FB_APP_ID
            }))
