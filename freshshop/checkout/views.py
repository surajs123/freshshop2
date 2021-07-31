from django.shortcuts import render

# Create your views here.

def checkhome(request):
    return render (request, 'checkout.html')



