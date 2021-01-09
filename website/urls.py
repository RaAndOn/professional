from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from . import views

urlpatterns = [
	url(r'^$', views.HomeView.as_view(), name='home'),
  url(r'^contact/$', views.ContactView.as_view(), name='contact'),
  url(r'^research/$', views.ResearchAllView.as_view(), name='research'),
  url(r'^teaching/$', views.TeachingAllView.as_view(), name='teaching'),
  path('tinymce/', include('tinymce.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)