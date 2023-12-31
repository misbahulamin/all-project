from django.shortcuts import render, redirect
from . models import TicketBook
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
# def home(request):
#     print(request.POST)
#     if request.method == 'POST':
#         fromlocation = request.POST.get('from')
#         tolocation = request.POST.get('to')
#         depaturedate = request.POST.get('deparure')
#         returndate = request.POST.get('return')
#         roundtrip = request.POST.get('roundtrip')
#         onewaytrip = request.POST.get('onewaytrip')
#         return render(request, 'index.html', {'fromlocation':fromlocation, 'tolocation':tolocation, 'depaturedate':depaturedate, 'returndate':returndate, 'roundtrip':roundtrip, 'onewaytrip':onewaytrip})
#     else:
#         return render(request, 'index.html')

def home(request):
    if request.method == 'POST':
        ticketData = forms.TicketBookForm(request.POST)
        if ticketData.is_valid():
            ticketData.save()
            return redirect('home')
    else:
        ticketData = forms.TicketBookForm()          
    return render(request, 'index.html', {'tickets': ticketData})

def contact(request):
    return render(request, 'contact.html')

def submitForm(request):
    return render(request, 'form.html')

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

def allData(request):
    cusData = TicketBook.objects.all()
    return render(request, 'data.html', {'tickets':cusData})

def deleteData(request, id):
    ticket = TicketBook.objects.get(pk = id)
    ticket.delete()
    return redirect('alldata')