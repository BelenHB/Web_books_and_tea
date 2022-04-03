from dataclasses import field
from django.shortcuts import render
from .models import Page

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

# Vista listado de BLOG (pages):
# def pages(request):
  
#   return render(request, 'pages/page_list.html')

class PageList(ListView):
  model = Page
  template_name = 'pages/page_list.html'
  
class PageDetail(DetailView):
  model = Page
  template_name = 'pages/page_detail.html'
  
class PageCreate(CreateView):
  model = Page
  fields = ['title', 'subtitle', 'content', 'author', 'created', 'image']
  success_url = '/pages/'
  
class PageUpdate(UpdateView):
  model = Page
  fields = ['title', 'subtitle', 'content', 'author', 'created', 'image']
  template_name = 'pages/page_update.html'
  success_url = '/pages/'
  
class PageDelete(DeleteView):
  model = Page
  success_url = '/pages/'
  