# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django import forms
from website import models

from tinymce.widgets import TinyMCE
from reversion.admin import VersionAdmin

from django import forms
from tinymce.widgets import TinyMCE

class ResearchAdminForm(forms.ModelForm):

    body = forms.CharField(widget=TinyMCE())

    class Meta:
        model = models.Research
        exclude = ()


class ResearchAdmin(VersionAdmin):
    list_display = ('id', 'title', 'order', 'featured', 'modified_datetime',)
    list_editable = ('title', 'order', 'featured',)
    fields = (
        'title',
        'body',
        'featured',
        )
    form = ResearchAdminForm

admin.site.register(models.Research, ResearchAdmin)


class TeachingAdminForm(forms.ModelForm):

    body = forms.CharField(widget=TinyMCE())

    class Meta:
        model = models.Teaching
        exclude = ()


class TeachingAdmin(VersionAdmin):
    list_display = ('id', 'title', 'order', 'featured', 'modified_datetime',)
    list_editable = ('title', 'order', 'featured',)
    fields = (
        'title',
        'body',
        'featured',
        )
    form = TeachingAdminForm

admin.site.register(models.Teaching, TeachingAdmin)


class CVAdminForm(forms.ModelForm):
    class Meta:
        model = models.CV
        exclude = ()

class CVAdmin(VersionAdmin):
    list_display = ('uploaded_at',)
    fields = (
        'document',
        )
    form = CVAdminForm

admin.site.register(models.CV, CVAdmin)
