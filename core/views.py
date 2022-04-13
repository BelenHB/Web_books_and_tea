from django.shortcuts import render

# Create your views here.

# Vista 'INICIO'
def home(request):
    return render(request, 'core/home.html', {})

  
# Vista 'ACERCA DE'
def about(request):
  return render(request, 'core/about.html', {})