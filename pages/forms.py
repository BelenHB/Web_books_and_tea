import re
from django import forms
from .models import Page
# from ckeditor.fields import RichTextFormField
from ckeditor.widgets import CKEditorWidget

# class PageForm(forms.Form):
#   title = forms.CharField(max_length=100, label='Título')
#   subtitle = forms.CharField(max_length=100, label='Subtítulo')
#   content = RichTextFormField(label='Contenido')
#   author = forms.CharField(max_length=50, label='Autor')
#   image = forms.ImageField(label='Imagen', null=True, blank=True)

  
  
class PageForm(forms.ModelForm):
  class Meta:
    model = Page
    fields = ['title', 'subtitle', 'content', 'author', 'image']
    widgets = {
      'title': forms.TextInput(),
      'subtitle': forms.TextInput(),
      'content': CKEditorWidget(),
      'author': forms.TextInput(),
      'image': forms.ImageField(),
    }
      
    