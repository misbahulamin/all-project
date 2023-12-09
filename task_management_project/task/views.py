from django.shortcuts import render, redirect
from . import forms
from . models import TaskModel

# Create your views here.

def home(request):
    return render(request, 'index.html')
def addTask(request):
    if request.method == 'POST':
        add_task = forms.TaskModelForm(request.POST)
        if add_task.is_valid():
            add_task.save()
            return redirect('taskshow')
    else:
        add_task = forms.TaskModelForm()     
    return render(request, 'addtask.html', {"form":add_task})

def showTask(request):
    alltask = TaskModel.objects.all()
    return render(request, 'taskshow.html', {"data": alltask})
def editTask(request, id):
    editData = TaskModel.objects.get(pk = id)
    edit_task_form = forms.TaskModelForm(instance=editData)
    if request.method == 'POST':
        edit_task_form = forms.TaskModelForm(request.POST, instance=editData)
        if edit_task_form.is_valid():
            edit_task_form.save()
            return redirect('taskshow')    
    return render(request, 'addtask.html', {"form":edit_task_form})

def deleteTask(request, id):
    delteData = TaskModel.objects.get(pk = id)
    delteData.delete()
    return redirect('taskshow')
