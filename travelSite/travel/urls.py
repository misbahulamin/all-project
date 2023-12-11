from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('contactus/', views.contact),
    path('form/', views.submitForm),
    path('login/', views.logIn, name='login'),
    path('alldata/', views.allData, name='alldata'),
    path('delete/<int:id>', views.deleteData, name = 'deleteticket'),
]