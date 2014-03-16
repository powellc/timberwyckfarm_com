from django.db import models
from datetime import datetime
from filer.fields.file import FilerFileField


class LiveManager(models.Manager):
    def get_queryset(self):
        return super(LiveManager, self).get_queryset().filter(published=True)


class Resource(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    resource_file = FilerFileField(null=True, blank=True)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True, editable=False)
    modified = models.DateTimeField(editable=False)

    objects = models.Manager()
    live_objects = LiveManager()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        self.modified = datetime.today()
        return super(Resource, self).save(*args, **kwargs)
