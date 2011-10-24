from django.conf.urls.defaults import *
from django.conf import settings
from django.views.static import serve
from unipath import FSPath as Path
from farm.models import Building, Field
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
    url(r'^tour/buildings/$', view=ListView.as_view(model=Building), name="fm-building-list"),
    url(r'^tour/buildings/(?P<slug>[-\w]+)/$', view=DetailView.as_view(model=Building), name="fm-building-detail"),

    url(r'^tour/fields/$', view=ListView.as_view(model=Field), name="fm-field-list"),
    url(r'^tour/fields/(?P<slug>[-\w]+)/$', view=DetailView.as_view(model=Field), name="fm-field-detail"),

    (r'^', include('farm.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^', include('articles.urls')),
)
urlpatterns+= patterns('django.contrib.flatpages.views',
    url(r'^tour/$', 'flatpage', {'url': '/tour/'}, name='fl-tour'),
    url(r'^education/$', 'flatpage', {'url': '/education/'}, name='fl-education'),
)
