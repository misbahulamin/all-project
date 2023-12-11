from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.

def signIn(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            signForm = RegisterForm(request.POST)
            if signForm.is_valid():
                messages.success(request, 'Account Created Succesfully.')
                signForm.save()
        else:
            signForm = RegisterForm()
        return render(request, 'signup.html', {"form": signForm})
    else:
        return redirect('home')

def logIn(request):
    if not request.user.is_authenticated:  
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data = request.POST)
            if form.is_valid():
                userName = form.cleaned_data['username']
                userPass = form.cleaned_data['password']
                user = authenticate(username = userName, password = userPass)
                if user is not None:
                    login(request, user)
                    return redirect('home')             
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {"form": form})
    else:
        return redirect('home')
    
def userLogout(request):
    logout(request)
    return redirect('login')

def passChange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'passchange.html', {'form': form})
        
def passChangeWithOldPass(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('home')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'passchange.html', {'form': form})