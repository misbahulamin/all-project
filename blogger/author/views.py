from django.shortcuts import render, redirect
from . import forms

# Create your views here.

def authorpage(reqeust):
    if reqeust.method == 'POST':
        author_form = forms.AuthorForm(reqeust.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('authors')
    else:
        author_form = forms.AuthorForm()
    return render(reqeust, 'author.html', {'form': author_form})
