from datetime import *
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel

from .managers import PublicManager

class Topic(TitleSlugDescriptionModel, TimeStampedModel):
    """
    Topic model class.
    """

    class Meta:
        verbose_name = _('Topic')
        verbose_name_plural = _('Topics')

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('notes-topic-detail', (), { 'slug': self.slug})


class Note(TimeStampedModel):
    """
    Note model class.

    A simple model to handle adding arbitrary numbers of notes to an animal profile.
    """
    topic=models.ForeignKey(Topic)
    date=models.DateField(_('Date'), default=datetime.now())
    content=models.TextField(_('Content'))
    rendered_content=models.TextField(_('Rendered content'), blank=True, null=True, editable=False)
    public=models.BooleanField(_('Public'), default=True)
    author=models.ForeignKey(User, blank=True, null=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey("content_type", "object_id")

    public_objects = PublicManager()
    objects = models.Manager()

    class Meta:
        verbose_name=_('Note')
        verbose_name_plural=_('Notes')

    @models.permalink
    def get_absolute_url(self):
        return ('notes-view', (), { 'pk': self.pk})

