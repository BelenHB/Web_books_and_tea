from django import forms

# Formulario para carga de libros 
class BookForm(forms.Form):
  title = forms.CharField(label='Título', required=True, 
                          widget=forms.TextInput(attrs={
                            'placeholder':'Ingresa título',
                            'class':'form-control'}))
  author = forms.CharField(label='Autor', required=True,
                           widget=forms.TextInput(attrs={
                            'placeholder':'Ingresa autor',
                            'class':'form-control'}))
  isbn = forms.IntegerField(label='ISBN', min_value=0, max_value=9999999999999,
                         help_text='Solo números, máx. 13 caracteres')
  
  
# Formulario de búsqueda de libros
class BookSearchForm(forms.Form):
  find_book = forms.CharField(label='',max_length=100, 
                              widget=forms.TextInput(attrs={
                                'placeholder':'ingresa término',
                                'class':'form-control'
                              })) 
  