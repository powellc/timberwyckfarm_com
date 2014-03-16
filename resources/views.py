from django.views.generic import ListView, DetailView

from .models import Resource


class ResourceListView(ListView):
    model = Resource
    queryset = Resource.live_objects.all()


class ResourceDetailView(DetailView):
    model = Resource
    queryset = Resource.live_objects.all()
