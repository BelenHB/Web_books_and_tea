from django.urls import path
from . import views

urlpatterns = [
    path('', views.PageList.as_view(), name='pages'),
    path('<int:pk>/', views.PageDetail.as_view(), name='page_detail'),
    path('create/', views.PageCreate.as_view(), name='page_create'),
    path('update/<int:pk>', views.PageUpdate.as_view(), name='page_update'),
    path('delete/<int:pk>', views.PageDelete.as_view(), name='page_delete'),
]
