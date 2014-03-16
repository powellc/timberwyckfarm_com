from django.conf.urls.defaults import url, patterns
from .views import ResourceDetailView, ResourceListView

urlpatterns = patterns(
    '',
    url(r'^$', view=ResourceListView.as_view(), name="resource-list"),
    url(r'^(?P<slug>[-\w]+)/$', view=ResourceDetailView.as_view(),
        name="resource-detail"),
)
