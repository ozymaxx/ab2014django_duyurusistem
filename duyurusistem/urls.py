from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'duyurusistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
	url(r'^create_post/$', 'duyurular.views.create_post', name='create_post'),
	url(r'^signup/$', 'duyurular.views.signup', name='signup'),
	url(r'^posts/$', 'duyurular.views.post_search', name='posts'),
	url(r'^posts/(?P<post_id>\d+)/$', 'duyurular.views.single_post', name='post'),
	url(r'^posts/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', 'duyurular.views.daily_post', name='dailypost'),
	url(r'^login/$', 'duyurular.views.login', name='login'),
    url(r'^admin/', include(admin.site.urls)),
)
