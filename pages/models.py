from django.db import models
from ckeditor.fields import RichTextField
from django.utils.timezone import now
from datetime import datetime, date
from django.contrib.auth.models import User

# Create your models here.

class Page(models.Model):
  title = models.CharField(max_length=100, verbose_name='Título')
  subtitle = models.CharField(max_length=100, verbose_name='Subtítulo')
  content = RichTextField(verbose_name='Contenido')
  author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
  created = models.DateField(auto_now_add=True , verbose_name='Fecha creación')
  image = models.ImageField(upload_to='pages/', null=True, blank=True, verbose_name='Imagen')
  
  def __str__(self):
    return self.title
  