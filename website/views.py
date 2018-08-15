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


class ProjectAllView(TemplateView):

  template_name = "projects_all.html"

  def get_context_data(self, **kwargs):
    projects = Project.objects.active.order_by('order')
    context = super(ProjectAllView, self).get_context_data(**kwargs)
    context['projects'] = projects
    return context


class ProjectView(DetailView):

  template_name = "project_detail.html"
  model = Project

  def get_context_data(self, **kwargs):
    context = super(ProjectView, self).get_context_data(**kwargs)
    return context


class ExperienceAllView(TemplateView):

  template_name = "experience_all.html"

  def get_context_data(self, **kwargs):
    experiences = Experience.objects.active.order_by('order')
    context = super(ExperienceAllView, self).get_context_data(**kwargs)
    context['experiences'] = experiences
    return context


class ExperienceView(DetailView):

  template_name = "experience_detail.html"
  model = Experience

  def get_context_data(self, **kwargs):
    context = super(ExperienceView, self).get_context_data(**kwargs)
    return context


class ResumeView(TemplateView):

  template_name = "resume.html"

  def get_context_data(self, **kwargs):
    context = super(ResumeView, self).get_context_data(**kwargs)
    return context