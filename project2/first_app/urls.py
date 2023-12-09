from django.urls import path
from . import views

urlpatterns = [
    
    # path("", include('first_app.urls'))
    path("",views.home),
]