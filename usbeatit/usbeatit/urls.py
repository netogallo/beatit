from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.home', name='home'),
    url(r'^home/board', 'home.views.board', name='board'),
    url(r'^home/save_post', 'home.views.save_post', name='save_post'),
    url(r'^home/delete_post', 'home.views.delete_post', name='delete_post'),
    url(r'^home/login', 'home.views.login', name='login'),
    url(r'^home/page/(?P<page_id>[0-9A-Za-z]+)', 'home.views.get_page', name='get_page'),
    url(r'^home/user_update', 'home.views.update_user_data', name='user_page_update'),
    url(r'^home/user_register', 'home.views.register_user', name='user_register'),
    url(r'home/user', 'home.views.get_user_page', name='user_page'),
    url(r'^admin/', include(admin.site.urls)),
   url(r'^accounts/', include('allauth.urls')),
    url(r'^ckeditor/', include('ckeditor.urls'))
)
