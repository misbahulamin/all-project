from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.categorypage, name = 'category')
]