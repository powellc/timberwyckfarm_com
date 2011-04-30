from django.conf.urls.defaults import *
from django.conf import settings
from django.views.static import serve
from unipath import FSPath as Path
#from timberwyckfarm_com.sitemap import TWFSitemap

#feeds = {
#   'events': UpcomingEvents,
#   'news': LatestNews,
#}

#sitemaps={
#    'site':TWFSitemap,
#}

if settings.DEBUG:
    urlpatterns = patterns('', 
        (r'^media/(?P<path>.*)$', serve, 
			{'document_root' : Path(__file__).parent.child("media")}),
    )
else:
    urlpatterns = patterns('',)

from django.contrib import admin
admin.autodiscover()

urlpatterns += patterns('',
    #(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
    #(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    (r'^', include('farm.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^', include('articles.urls')),
)
