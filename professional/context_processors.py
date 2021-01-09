from website.models import CV

def cv_context(request):
  cv = CV.objects.first()
  return { 'cv': cv }