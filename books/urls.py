from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list , name='book_list'),
    path('book_create/', views.book_create , name='book_create'),
    path('book_update/<int:id>', views.book_update , name='book_update'),
    path('book_delete/<int:id>', views.book_delete , name='book_delete'),
    path('book_search/', views.book_search, name='book_search'),
]
