from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('farmyard.urls')),
    (r'^calendar/', include('timberwyckfarm_com.apps.calendarium.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^blog/', include('timberwyckfarm_com.apps.articles.urls')),
    (r'^journal/', include('timberwyckfarm_com.apps.notes.urls')),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^education/$', 'flatpage', {'url': '/education/'},
        name='fl-education'),
)
