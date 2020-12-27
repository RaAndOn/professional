from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from . import views

urlpatterns = [
	url(r'^$', views.HomeView.as_view(), name='home'),
  url(r'^contact/$', views.ContactView.as_view(), name='contact'),
  url(r'^about/$', views.AboutView.as_view(), name='about'),
  url(r'^resume/$', views.ResumeView.as_view(), name='resume'),
  # url(r'^projects/$', views.ProjectAllView.as_view(), name='project-all'),
  # url(r'^projects/(?P<slug>[a-zA-Z0-9_-]+)/$', views.ProjectView.as_view(), name='project'),
  url(r'^experience/$', views.ExperienceAllView.as_view(), name='experience-all'),
  url(r'^experience/(?P<slug>[a-zA-Z0-9_-]+)/$', views.ExperienceView.as_view(), name='experience'),
  path('tinymce/', include('tinymce.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)