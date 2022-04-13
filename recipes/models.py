from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
  recipe_title = models.CharField(max_length=150, verbose_name='Receta')
  ingredients = RichTextField(verbose_name='Ingredientes')
  preparation = RichTextField(verbose_name='Preparación')
  author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
  picture = models.ImageField(upload_to='recipes/', null=True, blank=True, verbose_name='Foto')
  
  def __str__(self):
    return self.recipe_title
  
  
  
  
  