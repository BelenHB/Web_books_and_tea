from collections import UserDict
from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Se genera un formulario propio para el registro
class UserForm(UserCreationForm):
  username = forms.CharField(label='Usuario')
  email = forms.EmailField(label='email')
  password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
  password2 = forms.CharField(label='Confirma contraseña', widget=forms.PasswordInput())
  
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
    help_texts = {k:'' for k in fields}
    

# Formulario para hacer el perfil de usuario
class ProfileUserForm(forms.Form):
  email = forms.EmailField(label='email')
  password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(),
                              required=False)
  password2 = forms.CharField(label='Confirma contraseña', widget=forms.PasswordInput(),
                              required=False)
  first_name = forms.CharField(label='Nombre')
  last_name = forms.CharField(label='Apellido', required=False)
  avatar = forms.ImageField(label='Avatar', required=False)
  link = forms.URLField(label='Link', required=False)
  description = forms.CharField(label='Descripción', widget=forms.Textarea(), required=False)
  