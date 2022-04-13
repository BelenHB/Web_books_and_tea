from django.shortcuts import render

from pages.forms import PageForm
from .models import Page

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# Vista listado de BLOG (pages):
# def pages(request):
  
#   return render(request, 'pages/page_list.html')

class PageList(ListView):
  model = Page
  template_name = 'pages/page_list.html'
  ordering = ['-created']
  
class PageDetail(DetailView):
  model = Page
  template_name = 'pages/page_detail.html'
  
class PageCreate(LoginRequiredMixin, CreateView):
  model = Page
  # fields = ['title', 'subtitle', 'content', 'author', 'image']
  form_class = PageForm
  success_url = '/pages/'
  
class PageUpdate(LoginRequiredMixin, UpdateView):
  model = Page
  # fields = ['title', 'subtitle', 'content', 'author', 'image']
  form_class = PageForm
  template_name = 'pages/page_update.html'
  success_url = '/pages/'
  
class PageDelete(LoginRequiredMixin, DeleteView):
  model = Page
  success_url = '/pages/'
  