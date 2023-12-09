from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def profile(request):
    if request.method == 'POST':
        profile_forms = forms.ProfileForm(request.POST)
        if profile_forms.is_valid():
            profile_forms.save()
            return redirect('profile')
    else:
        profile_forms = forms.ProfileForm()
    return render(request, 'profile.html', {'form': profile_forms})