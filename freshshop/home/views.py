from django.shortcuts import render
from custamor.models import onlineuser, CartModelFruite, CartModelvegitable

# Create your views here.

def index(request):
    count1 = CartModelFruite.objects.all().count()
    count2 = CartModelvegitable.objects.all().count()
    count = count1+count2

    return render (request, 'index.html',{'count':count} )



def check (request):
    return render(request, 'checkout.html') 

