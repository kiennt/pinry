from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from pinry.admin import *

urlpatterns = patterns('',
    url(r'', include('social_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('pinry.api.urls', namespace='api')),
    url(r'^pins/', include('pinry.pins.urls', namespace='pins')),
    url(r'', include('pinry.core.urls', namespace='core')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
