from django.shortcuts import redirect, render

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserForm, ProfileUserForm

from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.

# Vista LOGIN
def user_login(request):
  
  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
  
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      
      user = authenticate(username=username, password=password)
      
      if user is not None:
        msg = 'Bienvenido usuario registrado'
        login(request, user)
        return redirect('home')
        # return render(request, 'core/home.html', {'msg':msg})
      else:
        msg = 'Usuario o contraseña no válido'
        return render(request, 'login.html', {'form':form, 'msg':msg})
      
    else:
      msg = 'Datos erróneos'
      return render(request, 'login.html', {'form':form, 'msg':msg})
      
  else:
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})
    

# Vista REGISTRARSE
def signup(request):

  if request.method == 'POST':
    # form = UserCreationForm(request.POST) #este form ya viene de django
    form = UserForm(request.POST) #se usa uno creado por nosotros
    if form.is_valid():
      username = form.cleaned_data['username']
      form.save()
      # return render(request, 'core/home.html')
      # form = AuthenticationForm()
      # return render(request, 'registration/login.html', {'form':AuthenticationForm()})
      return redirect('login')
      
    else:
      print('entra al else')
      return render(request, 'signup.html', {'form':form, 'msg':'Formulario no válido'})
      # print('form no valido, entra al else')
      # return render(request, 'registration/register.html', {'form':form})
          
  form = UserForm()
  print('va por afuera')
  return render(request, 'signup.html', {'form':form})

# Vista EDITAR PERFIL
# @login_required
# def edit_user(request):
#   msg = ''
#   logged_user = request.user
#   if request.method == 'POST':
#     form = UserEditForm(request.POST)
#     if form.is_valid():
#       data = form.cleaned_data
      
#       logged_user.email = data.get('email')
#       logged_user.first_name = data.get('first_name', '')
#       logged_user.last_name = data.get('last_name', '')
      
#       if data.get('password1') == data.get('password2') and len(data.get('password1')) >= 8:
#         logged_user.set_password(data.get('password1'))
#       else:
#         msg = 'La contraseña no se ha modificado' 
      
#       logged_user.save()
      
#       return render(request, 'core/home.html', {'msg':msg})
    
#     else:
#       msg = 'Datos no válidos'
#       return render(request, 'edit_user.html', {'form':form, 'msg':msg})
  
#   form = UserEditForm(
#     initial={
#       'username': logged_user.username,
#       'email': logged_user.email,
#       'first_name': logged_user.first_name,
#       'last_name': logged_user.last_name,      
#     })
  
#   return render(request, 'edit_user.html', {'form':form, 'msg':msg})#, 'img_avatar':show_avatar(request.user)})


# @login_required
# def show_avatar(user):
#   return UserAvatar.objects.filter(user=user.id)[0].image.url

@login_required
def show_avatar(user):
  # profile_user, _ = Profile.objects.get_or_create(user=user)
  # if profile_user.avatar:
  #   avatar = profile_user.avatar.url
  # else:
  #   avatar = None
#   # return render(request, 'edit_profile.html', {'profile_user':profile_user})
  return Profile.objects.filter(user=user.id)[0].avatar.url
  # return avatar

@login_required
def edit_profile_user(request):
  logged_user, _ = Profile.objects.get_or_create(user=request.user)
  if request.method == 'POST':
    form = ProfileUserForm(request.POST, request.FILES)
    
    if form.is_valid():
      request.user.email = form.cleaned_data['email']
      request.user.first_name = form.cleaned_data['first_name']
      request.user.last_name = form.cleaned_data['last_name']
      logged_user.avatar = form.cleaned_data['avatar']
      logged_user.link = form.cleaned_data['link']
      logged_user.description = form.cleaned_data['description']
      
      if form.cleaned_data['password1'] != '' and form.cleaned_data['password1'] == form.cleaned_data['password2']:
        request.user.set_password(form.cleaned_data['password1'])
      
      request.user.save()
      print(f'este es el {request.user}')
      logged_user.save()
      print(f'este es el logged_user {logged_user}')
      
      return redirect('home')
    
    else:
      return render(request, 'signup.html', {'form':form})
  
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
  
  return render(request, 'edit_profile.html', {'form':form})

# @login_required
# def show_avatar(request):
#     logged_user, _ = Profile.objects.get_or_create(user=request.user)
#     return render(request, 'edit_profile.html', {'logged_user':logged_user})