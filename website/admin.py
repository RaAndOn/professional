# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django import forms
from website import models

from tinymce.widgets import TinyMCE
from reversion.admin import VersionAdmin

from django import forms
from tinymce.widgets import TinyMCE


class ProjectAdminForm(forms.ModelForm):
    short_description = forms.CharField(widget=TinyMCE())
    body = forms.CharField(widget=TinyMCE())

    class Meta:
        model = models.Project
        exclude = ()


class ProjectAdmin(VersionAdmin):
    list_display = ('id', 'title', 'subtitle', 'slug', 'order', 'featured', 'modified_datetime',)
    list_editable = ('title', 'subtitle', 'order', 'featured',)
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


class ExperienceAdminForm(forms.ModelForm):
    short_description = forms.CharField(widget=TinyMCE())
    body = forms.CharField(widget=TinyMCE())

    class Meta:
        model = models.Experience
        exclude = ()


class ExperienceAdmin(VersionAdmin):
    list_display = ('id', 'title', 'subtitle', 'slug', 'order', 'featured', 'modified_datetime',)
    list_editable = ('title', 'subtitle', 'order', 'featured',)
    fields = (
        'title',
        'subtitle',
        'image',
        'wide_image',
        'short_description',
        'body',
        'featured',
        )
    form = ExperienceAdminForm

admin.site.register(models.Experience, ExperienceAdmin)


class ResumeAdminForm(forms.ModelForm):
    class Meta:
        model = models.Resume
        exclude = ()

class ResumeAdmin(VersionAdmin):
    list_display = ('uploaded_at',)
    fields = (
        'document',
        )
    form = ResumeAdminForm

admin.site.register(models.Resume, ResumeAdmin)


class HomeImageAdminForm(forms.ModelForm):
    class Meta:
        model = models.HomeImage
        exclude = ()

class HomeImageAdmin(VersionAdmin):
    list_display = ('uploaded_at',)
    fields = (
        'image',
        )
    form = HomeImageAdminForm

admin.site.register(models.HomeImage, HomeImageAdmin)