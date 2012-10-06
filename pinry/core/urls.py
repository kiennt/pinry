from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'pinry.core.views.home', name='home'),
    url(r'^private/$', 'pinry.core.views.private', name='private'),
    url(r'^login/$', 'pinry.core.views.login_user', name='login'),
    url(r'^register/$', 'pinry.core.views.register', name='register'),
    url(r'^logout/$', 'pinry.core.views.logout_user', name='logout'),
)
