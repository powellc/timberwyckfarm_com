from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from django.db import models
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld


class FlatPageAdmin(FlatPageAdminOld):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
