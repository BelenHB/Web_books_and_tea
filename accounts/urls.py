from django import views
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('edit_user/', views.edit_user, name='edit_user'),
]
