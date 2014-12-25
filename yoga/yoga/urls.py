from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('apps.users.urls')),
    url(r'^', include('apps.classes.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
