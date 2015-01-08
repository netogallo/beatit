from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.home', name='home'),
    url(r'^home/board', 'home.views.board', name='board'),
    url(r'^home/save_post', 'home.views.save_post', name='save_post'),
    url(r'^admin/', include(admin.site.urls)),
   url(r'^accounts/', include('allauth.urls')),
    url(r'^ckeditor/', include('ckeditor.urls'))
)
