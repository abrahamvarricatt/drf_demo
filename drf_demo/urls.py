from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'drf_demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^display/', include('display.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
