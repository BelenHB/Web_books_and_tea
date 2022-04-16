from django.shortcuts import render
from .forms import RecipeForm
from .models import Recipe

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class RecipeList(ListView):
  model = Recipe
  template_name = 'recipes/recipe_list.html'
  ordering = ['-id']

  
class RecipeDetail(DetailView):
  model = Recipe
  template_name = 'recipes/recipe_detail.html'
  
class RecipeCreate(LoginRequiredMixin, CreateView):
  model = Recipe
  fields = ['recipe_title', 'ingredients', 'preparation', 'author', 'picture']
  success_url = '/recipes/'
  
class RecipeUpdate(LoginRequiredMixin, UpdateView):
  model = Recipe
  fields = ['recipe_title', 'ingredients', 'preparation', 'author', 'picture']
  template_name = 'recipes/recipe_update.html'
  success_url = '/recipes/'
  
class RecipeDelete(LoginRequiredMixin, DeleteView):
  model = Recipe
  success_url = '/recipes/'
  