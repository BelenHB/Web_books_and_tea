from django.shortcuts import render

# para mostrar el avatar
from accounts.views import show_avatar

# Create your views here.

# Vista 'home'
def home(request):
    return render(request, 'core/home.html', {})#'img_avatar':show_avatar(request.user)})

  

def about(request):
  return render(request, 'core/about.html', {})#'img_avatar':show_avatar(request.user)})