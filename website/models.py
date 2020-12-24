# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from autoslug import AutoSlugField
from autoslug.settings import slugify as default_slugify
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from tinymce.models import HTMLField

""" Featured Status Constants """
INACTIVE = 1   # not displayed
FEATURED = 2   # visible and featured
ACTIVE = 3   # shown everywhere except for featured page
FEATURED_CHOICES = (
        (INACTIVE, 'inactive'),
        (ACTIVE, 'active'),
        (FEATURED, 'featured'),
        )


class FeatureManager(models.Manager):
    """ Manager for featured models. """

    @property
    def featured(self):
        return self.filter(featured=FEATURED).order_by('?')

    @property
    def active(self):
        return self.filter(featured__in=[ACTIVE, FEATURED]).order_by('title')

    @property
    def unfeatured(self):
        return self.filter(featured=ACTIVE).order_by('title')


class FeatureMixin(models.Model):
    """ Mixin with common fields for Capability, Project and Staff  """

    class Meta:
        abstract = True

    objects = FeatureManager()

    title = models.CharField(max_length=64)
    subtitle = models.CharField(max_length=64, blank=True, null=True)
    image = models.ImageField(
            'Index Page Image',
            upload_to='images',
            height_field=None,
            width_field=None,
            null=True,
            blank=True,
            help_text='Model Image',
            )
    wide_image = models.ImageField(
            'Detail Page Image',
            upload_to='images',
            height_field=None,
            width_field=None,
            null=True,
            blank=True,
            )
    slug = AutoSlugField(
            populate_from='generate_slug',
            unique=True,
            help_text='URL key for the instance (automatically populated from title). You should generally not change this field as you\'ll break deep links to the instance.',
            )
    body = HTMLField(max_length=64 * 1024, blank=True, null=True)
    short_description = models.CharField(
            max_length=500,
            default='',
            help_text='Brief description to show in smaller content areas',
            )
    featured = models.IntegerField(
            'Display',
            choices=FEATURED_CHOICES,
            default=INACTIVE,
            help_text='Inactive = not displayed, Active = Displayed everywhere except Featured page, Featured = Displayed everywhere including Featured page',
            )
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    order = models.IntegerField(default=1)

    def generate_slug(self):
        return default_slugify(self.title)

    def heading(self):
        return "{0} - {1}".format(self.title, self.subtitle)


class Project(FeatureMixin):
    """ Project model  """

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return ('projects', [self.slug])


class Experience(FeatureMixin):
    """ Experience model  """

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return ('experience', [self.slug])


class Resume(models.Model):
    def __unicode__(self):
        return "Resume"

    objects = FeatureManager()

    document = models.FileField(upload_to='documents')
    uploaded_at = models.DateTimeField(auto_now_add=True)