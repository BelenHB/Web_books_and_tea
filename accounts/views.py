from django.shortcuts import redirect, render

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserForm, ProfileUserForm

from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.

# Vista INGRESAR
def user_login(request):
  
  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
  
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      
      user = authenticate(username=username, password=password)
      
      if user is not None:
        login(request, user)
        return redirect('home')

      else:
        msg = 'Usuario o contraseña no válido'
        return render(request, 'accounts/login.html', {'form':form, 'msg':msg})
      
    else:
      msg = 'Datos erróneos'
      return render(request, 'accounts/login.html', {'form':form, 'msg':msg})
      
  else:
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})
    

# Vista REGISTRARSE
def signup(request):

  if request.method == 'POST':
    form = UserForm(request.POST) #se usa un formulario personalizado por nosotros
    
    if form.is_valid():
      username = form.cleaned_data['username']
      form.save()
      return redirect('login')
      
    else:
      return render(request, 'accounts/signup.html', {'form':form, 'msg':'Formulario no válido'})
         
  form = UserForm()
  return render(request, 'accounts/signup.html', {'form':form})


# Vista EDITAR PERFIL (se accede clickeando sobre el avatar de usuario y luego
# el botón de 'Editar perfil')
@login_required
def edit_profile_user(request):
  
  logged_user, _ = Profile.objects.get_or_create(user=request.user)
  
  if request.method == 'POST':
    form = ProfileUserForm(request.POST, request.FILES)
    
    if form.is_valid():
      data = form.cleaned_data

      request.user.email = data.get('email',)
      request.user.first_name = data.get('first_name')
      request.user.last_name = data.get('last_name', '')      
      
      # recuperar la imagen de avatar si hubiera
      avatar = data.get('avatar', '')

      if avatar is not None:        
        if avatar is False:
          logged_user.avatar = None          
        else:
          logged_user.avatar = data.get('avatar')
          
      logged_user.link = data.get('link', '')
      logged_user.description = data.get('description','')
      
      # comprobar si se modifica la contraseña, y si es así, cambiarla
      if data.get('password1') != '' and data.get('password1') == data.get('password2'):
        request.user.set_password(data.get('password1'))
      
      request.user.save()
      logged_user.save()
     
      return redirect('home')
    
    else:
      return render(request, 'accounts/edit_profile.html', {'form':form})
  
  form = ProfileUserForm(initial= 
                         {
                           'email': request.user.email,
                           'password1': '',
                           'password2': '',
                           'first_name': request.user.first_name,
                           'last_name': request.user.last_name,
                           'avatar': logged_user.avatar,
                           'link': logged_user.link,
                           'description': logged_user.description,  
                         })
  
  return render(request, 'accounts/edit_profile.html', {'form':form})


# Vista de PERFIL DE USUARIO
@login_required
def user_profile(request):
  return render(request, 'accounts/profile.html', {})


# Vista de USUARIOS (listado de perfiles registrados)
def profiles_list(request):
  profiles = Profile.objects.all()
  return render(request, 'accounts/profiles_list.html', {'profiles':profiles})