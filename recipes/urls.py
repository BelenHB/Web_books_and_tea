from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecipeList.as_view(), name='recipes'),
    path('create/', views.RecipeCreate.as_view(), name='recipe_create'),
    path('update/<int:pk>', views.RecipeUpdate.as_view(), name='recipe_update'),
    path('<int:pk>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('delete/<int:pk>', views.RecipeDelete.as_view(), name='recipe_delete'),
]
