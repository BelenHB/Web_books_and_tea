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
      print('entra al else')
      return render(request, 'accounts/signup.html', {'form':form, 'msg':'Formulario no válido'})
      # print('form no valido, entra al else')
      # return render(request, 'registration/register.html', {'form':form})
          
  form = UserForm()
  print('va por afuera')
  return render(request, 'accounts/signup.html', {'form':form})





@login_required
def edit_profile_user(request):
  logged_user, _ = Profile.objects.get_or_create(user=request.user)
  if request.method == 'POST':
    form = ProfileUserForm(request.POST, request.FILES)
    
    if form.is_valid():
      request.user.email = form.cleaned_data['email']
      request.user.first_name = form.cleaned_data['first_name']
      request.user.last_name = form.cleaned_data['last_name']
      if form.cleaned_data['avatar']:
        logged_user.avatar = form.cleaned_data['avatar']
      else:
        print(logged_user.avatar)
      logged_user.link = form.cleaned_data['link']
      logged_user.description = form.cleaned_data['description']
      
      if form.cleaned_data['password1'] != '' and form.cleaned_data['password1'] == form.cleaned_data['password2']:
        request.user.set_password(form.cleaned_data['password1'])
      
      request.user.save()
      logged_user.save()
     
      return redirect('home')
    
    else:
      return render(request, 'accounts/signup.html', {'form':form})
  
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


@login_required
def user_profile(request):
  return render(request, 'accounts/user_profile.html', {})

