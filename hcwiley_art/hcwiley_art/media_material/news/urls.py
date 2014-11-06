from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'media_material.news.views.home', name='home'),
     url(r'^/archive images/(?P<path>.*)$', 'media_material.news.views.news_image'),
     url(r'^/[\d]+-[\d]+-[\d]+-(?P<pk>.*)$', 'media_material.news.views.news'),
)
