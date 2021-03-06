from django import views
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('edit_profile/', views.edit_profile_user, name='edit_profile'),
    path('profiles_list/', views.profiles_list, name='profiles_list'),
]
