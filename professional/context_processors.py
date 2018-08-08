from website.models import Resume

def resume_context(request):
  resume = Resume.objects.first()
  return { 'resume': resume }