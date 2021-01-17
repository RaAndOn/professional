from website.models import Resume, HomeImage

def resume_context(request):
  resume = Resume.objects.first()
  return { 'resume': resume }

def home_image_context(request):
  home_image = HomeImage.objects.first()
  return { 'home_image': home_image }