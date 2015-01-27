from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Data.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'tags/', include('tags.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
