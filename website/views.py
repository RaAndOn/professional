# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView

class HomeView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

# def home(request):
# 	template = loader.get_template('home.html')
# 	return HttpResponse(template.render(context, request))
