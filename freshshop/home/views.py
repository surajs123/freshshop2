from django.db.models.query_utils import Q
from django.http.response import JsonResponse
from django.shortcuts import render
from custamor.models import onlineuser, CartModelFruite, CartModelvegitable
from fruit.models import fruits
from vegetable.models import vegitable

# Create your views here.

def index(request):
    count1 = CartModelFruite.objects.all().count()
    count2 = CartModelvegitable.objects.all().count()
    count = count1+count2

    return render (request, 'index.html',{'count':count} )



def check (request):
    return render(request, 'checkout.html') 

def autocom(request):
    if 'term' in request.GET:
        nam = request.GET['term']
        print(nam)
        qs1 = fruits.objects.filter(Q(name__istartswith=nam))
        qs2 = vegitable.objects.filter(Q(name__istartswith=nam))
        print(qs1)
        name1 = list()
        name2 = list()
        namet = list()
        for fruit in qs1:
            name1.append(fruit.name)
            print(name1)
        for fruit in qs2:
            name2.append(fruit.name)
            print(name2) 

        namet = name1+name2       
        return JsonResponse(namet, safe=False) 
        

    return render(request, 'index.html')

def surch(request):
    pass          
    