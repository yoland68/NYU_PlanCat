from django.conf.urls import patterns, include, url
from django.contrib import admin
from basic import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'falbert.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^courses/', include(admin.site.urls)),
)
