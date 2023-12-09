from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('create_post/', views.createPost, name = 'createpost'),
    path('edit/<int:id>', views.editPost, name = 'editpost'),
    path('delete/<int:id>', views.deletePost, name = 'deletepost'),
]
