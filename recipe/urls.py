from django.urls import path, include
from recipe import views
from rest_framework import routers

# router define automatically rest routes
recipe_router = routers.DefaultRouter(trailing_slash=False)
recipe_router.register('recipe', views.RecipeView)
recipe_router.register('tag', views.TagView)
recipe_router.register('ingredient', views.IngredientView)

urlpatterns = [
    path('', include(recipe_router.urls))
]
