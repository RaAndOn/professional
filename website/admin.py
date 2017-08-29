# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django import forms
from website import models

from tinymce.widgets import TinyMCE
from reversion.admin import VersionAdmin

class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = models.Project
        widgets = {'short_description': TinyMCE,}
        exclude = ()


class ProjectAdmin(VersionAdmin):
    list_display = ('id', 'title', 'subtitle', 'slug', 'featured', 'modified_datetime',)
    list_editable = ('title', 'subtitle', 'featured',)
    fields = (
        'title',
        'subtitle',
        'image',
        'wide_image',
        'short_description',
        'body',
        'featured',
        )
    form = ProjectAdminForm

admin.site.register(models.Project, ProjectAdmin)
