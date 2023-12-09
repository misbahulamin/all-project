from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('addtask/', views.addTask, name = 'addtask'),
    path('taskshow/', views.showTask, name = 'taskshow'),
    path('editTask/<int:id>', views.editTask, name='edittask'),
    path('deltetask/<int:id>', views.deleteTask, name='deletetask')
]