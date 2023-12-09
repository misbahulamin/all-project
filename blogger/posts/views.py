from django.shortcuts import render, redirect
from . import forms
from posts.models import Post

# Create your views here.
def home(request):
    data = Post.objects.all()
    return render(request, 'article.html', {'datas':data})
def createPost(request):
    if request.method == 'POST':
        post_forms = forms.PostForm(request.POST)
        if post_forms.is_valid():
            post_forms.save()
            return redirect('createpost')
    else:
        post_forms = forms.PostForm()
    return render(request, 'createarticle.html', {'form': post_forms})

def editPost(request, id):
    post = Post.objects.get(pk = id)
    post_forms = forms.PostForm(instance = post)
    if request.method == 'POST':
        post_forms = forms.PostForm(request.POST, instance = post)
        if post_forms.is_valid():
            post_forms.save()
            return redirect('home')
    return render(request, 'createarticle.html', {'form': post_forms})

def deletePost(request, id):
    post = Post.objects.get(pk = id)
    post.delete()
    return redirect('home')