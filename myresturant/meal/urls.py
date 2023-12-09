from django.urls import path

from . import views
urlpatterns = [
    path("", views.home),
    path("meal/", views.mealDetails)
]