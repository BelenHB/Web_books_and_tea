from django.db import models

# Create your models here.

# Modelo LIBRO (Book)
class Book(models.Model):
  title = models.CharField(max_length=100, verbose_name='Título')
  author = models.CharField(max_length=100, verbose_name='Autor')
  isbn = models.PositiveIntegerField(verbose_name='ISBN')
  
  def __str__(self):
      return self.title
