from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    data = {'karim': 'Karim', 'rahim':'Rahim', 'towaha':'Towaha'}
    context = {'data':data}
    return render(request, 'contact.html', context)
