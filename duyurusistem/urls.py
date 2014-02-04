from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'duyurusistem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
	url(r'^create_post/$', 'duyuru.views.create_post', name='home'),
	url(r'^signup/$', 'duyuru.views.signup', name='home'),
	url(r'^posts/$', 'duyuru.views.post_search', name='home'),
	url(r'^posts/(?P<post_id>\d+)/$', 'duyurusistem.views.single_post', name='home'),
	url(r'^posts/$', 'duyurusistem.views.daily_post', name='home'),
	url(r'^login/$', 'duyuru.views.login', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
