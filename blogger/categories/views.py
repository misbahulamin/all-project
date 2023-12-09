from django.shortcuts import render, redirect
from .import forms

# Create your views here.
def categorypage(reqeust):
    return render(reqeust, 'category.html')

def categorypage(request):
    if request.method == 'POST':
        category_forms = forms.CategoryForm(request.POST)
        if category_forms.is_valid():
            category_forms.save()
            return redirect('category')
    else:
        category_forms = forms.CategoryForm()
    return render(request, 'category.html', {'form': category_forms})