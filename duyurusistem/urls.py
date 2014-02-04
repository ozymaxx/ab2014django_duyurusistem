from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'duyurusistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
	url(r'^create_post/$', 'duyurular.views.create_post', name='home'),
	url(r'^signup/$', 'duyurular.views.signup', name='home'),
	url(r'^posts/$', 'duyurular.views.post_search', name='home'),
	url(r'^posts/(?P<post_id>\d+)/$', 'duyurular.views.single_post', name='home'),
	url(r'^posts/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', 'duyurular.views.daily_post', name='home'),
	url(r'^login/$', 'duyurular.views.login', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
