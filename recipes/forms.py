from django import forms
from .models import Recipe
from ckeditor.fields import RichTextFormField
from django.contrib.auth.models import User


class RecipeForm(forms.Form):
  recipe_title = forms.CharField(label='Receta', required=True, 
                          widget=forms.TextInput(attrs={'class':'form-control'}))
  ingredients = RichTextFormField(label='Ingredientes')
  preparation = RichTextFormField(label='Preparación')
  picture = forms.ImageField(label='Foto', required=False)
  

  