
from django.conf.urls import patterns, url

from timberwyckfarm_com.apps.homepage.views import HomepageView

urlpatterns = patterns('',
    url(r'^$', HomepageView.as_view(), name='homepage'),
)
