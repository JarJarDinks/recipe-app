from django.urls import path
from .views import RecipeListView, RecipeDetailView, HomeView, AddRecipe
from . import views

app_name = "recipes"

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("recipe/", RecipeListView.as_view(), name="recipe"),
    path("recipe/<int:pk>/", RecipeDetailView.as_view(), name="detail"),
    path("recipe/add/", AddRecipe.as_view(), name="add"),
    path('recipe/<int:recipe_id>/delete/', views.delete_recipe, name='delete_recipe'),
    path('like/<int:recipe_id>/', views.like_recipe, name='like_recipe'),
]
