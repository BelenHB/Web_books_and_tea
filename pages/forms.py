from django import forms
from .models import Page
# from ckeditor.fields import RichTextFormField
from ckeditor.widgets import CKEditorWidget

# class PageForm(forms.Form):
#   title = forms.CharField(label='Título',required=True, widget=forms.TextInput(
#     attrs={'placeholder':'ingrese título', 'class':'form-control'}))
#   subtitle = forms.CharField(label='Subtítulo', widget=forms.TextInput(
#     attrs={'placeholder':'ingrese subtítulo', 'class':'form-control'}))
#   content = RichTextFormField(label='Contenido')
#   author = forms.CharField(label='Autor', widget=forms.TextInput(
#     attrs={'placeholder':'ingrese autor', 'class':'form-control'}))
#   image = forms.ImageField(label='Imagen', null=True, blank=True)


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
      
    