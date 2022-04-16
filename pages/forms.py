from django import forms
from .models import Page

from ckeditor.widgets import CKEditorWidget

# Utilizo la herencia del modelo para crear el formulario 
class PageForm(forms.ModelForm):
  class Meta:
    model = Page
    fields = ['title', 'subtitle', 'content', 'author', 'image']
    widgets = {
      'title': forms.TextInput(attrs={'class':'form-control'}),
      'subtitle': forms.TextInput(attrs={'class':'form-control'}),
      'content': CKEditorWidget(),
    }
      
    