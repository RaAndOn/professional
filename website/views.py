# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from django.views.generic import DetailView

from website.models import *

class HomeView(TemplateView):

  template_name = "home.html"

  def get_context_data(self, **kwargs):
    context = super(HomeView, self).get_context_data(**kwargs)
    return context


class ContactView(TemplateView):

  template_name = "contact.html"

  def get_context_data(self, **kwargs):
    context = super(ContactView, self).get_context_data(**kwargs)
    return context


class AboutView(TemplateView):

  template_name = "about.html"

  def get_context_data(self, **kwargs):
    context = super(AboutView, self).get_context_data(**kwargs)
    return context


class TeachingAllView(TemplateView):

  template_name = "teaching_all.html"

  def get_context_data(self, **kwargs):
    teaching = Teaching.objects.active.order_by('order')
    context = super(TeachingAllView, self).get_context_data(**kwargs)
    context['teaching'] = teaching
    return context


class ResearchAllView(TemplateView):

  template_name = "research_all.html"

  def get_context_data(self, **kwargs):
    research = Research.objects.active.order_by('order')
    context = super(ResearchAllView, self).get_context_data(**kwargs)
    context['research'] = research
    return context


class ResumeView(TemplateView):

  template_name = "resume.html"

  def get_context_data(self, **kwargs):
    context = super(ResumeView, self).get_context_data(**kwargs)
    return context