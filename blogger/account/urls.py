from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.signIn , name = 'signup'),
    path('login/', views.logIn , name = 'login'),
    path('logout/', views.userLogout , name = 'logout'),
    path('passchange/', views.passChange , name = 'passchange'),
    path('passchangewithoutoldpass/', views.passChangeWithOldPass , name = 'passchangewithoutoldpass'),
]
