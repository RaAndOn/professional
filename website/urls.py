from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	url(r'^$', views.HomeView.as_view(), name='home'),
  url(r'^contact/$', views.ContactView.as_view(), name='contact'),
  url(r'^about/$', views.AboutView.as_view(), name='about'),
  url(r'^resume/$', views.ResumeView.as_view(), name='resume'),
  url(r'^projects/$', views.ProjectAllView.as_view(), name='project-all'),
  url(r'^projects/(?P<slug>[a-zA-Z0-9_-]+)/$', views.ProjectView.as_view(), name='project'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)