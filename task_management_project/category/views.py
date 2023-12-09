from django.shortcuts import render, redirect
from . import forms

# Create your views here.

def addCategory(request):
    if request.method == 'POST':
        categoryformdata = forms.CategoryModelForm(request.POST)
        print(categoryformdata)
        if categoryformdata.is_valid():
            categoryformdata.save()
            return redirect('addtask')
    else:
        categoryformdata = forms.CategoryModelForm()
    return render(request, 'addcategory.html', {"form":categoryformdata})
