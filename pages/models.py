from django.db import models
from ckeditor.fields import RichTextField
from django.utils.timezone import now

# Create your models here.

class Page(models.Model):
  title = models.CharField(max_length=100, verbose_name='Título')
  subtitle = models.CharField(max_length=100, verbose_name='Subtítulo')
  content = RichTextField(verbose_name='Contenido')
  author = models.CharField(max_length=50, verbose_name='Autor')
  created = models.DateTimeField(default=now, verbose_name='Fecha creación')
  image = models.ImageField(upload_to='pages/', null=True, blank=True, verbose_name='Imagen')
  
  def __str__(self):
    return self.title