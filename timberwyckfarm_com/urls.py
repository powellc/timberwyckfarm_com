from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('timberwyckfarm_com.apps.homepage.urls')),
    (r'^', include('farmyard.urls')),
    (r'^calendar/', include('timberwyckfarm_com.apps.calendarium.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^blog/', include('timberwyckfarm_com.apps.articles.urls')),
    (r'^journal/', include('timberwyckfarm_com.apps.notes.urls')),
    (r'^ckeditor/', include('ckeditor.urls')),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^education/$', 'flatpage', {'url': '/education/'},
        name='fl-education'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    ) + urlpatterns
