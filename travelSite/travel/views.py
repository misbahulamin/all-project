from django.shortcuts import render

# Create your views here.
def home(request):
    print(request.POST)
    if request.method == 'POST':
        fromlocation = request.POST.get('from')
        tolocation = request.POST.get('to')
        depaturedate = request.POST.get('deparure')
        returndate = request.POST.get('return')
        roundtrip = request.POST.get('roundtrip')
        onewaytrip = request.POST.get('onewaytrip')
        return render(request, 'index.html', {'fromlocation':fromlocation, 'tolocation':tolocation, 'depaturedate':depaturedate, 'returndate':returndate, 'roundtrip':roundtrip, 'onewaytrip':onewaytrip})
    else:
        return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def submitForm(request):
    return render(request, 'form.html')