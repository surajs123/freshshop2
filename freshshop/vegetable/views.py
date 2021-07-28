from django.db.models.query_utils import Q
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .models import vegitable, vegreview
# Create your views here.
qtyv = vegitable.objects.all()
count1 =0
typ = 'vegita'
for totv in qtyv:
    count1 =count1+totv.quanty


def vegi(request):
    if request.method == 'POST':
        value = request.POST['search']
        obj = vegitable.objects.filter(name=value)

        return render(request, 'shop.html',{'food':obj, 'qty':count1, 'cata':' VEGITABLE ', 'act2':'active', 'typ':typ})
    
    else:
        food = vegitable.objects.all()
        return render(request, 'shop.html',{'food':food, 'qty':count1, 'cata':' VEGITABLE ', 'act2':'active', 'typ':typ})

def vdetail(request):
    
    val = request.GET['product']
    obj = vegitable.objects.get(id=val)
    food2 = vegitable.objects.all()
    rev = vegreview.objects.filter(product_id=obj)
    return render(request, 'shop-detail.html',{'obj':obj,'food':food2, 'rev':rev, 'typ':typ})  


def vegview(request):
    if request.method == 'POST':
        reviews = request.POST['review']
        pro_id =  request.POST['product']

        
        
       
        
        if reviews =="":
            print ('pleses enter the value ...')
        else:
            
            print ('poda patty')
            costamor_nam = request.POST['cos_name']
            obj = vegitable.objects.get(id = pro_id)
            product_id = obj
            product_name = obj.name
            rev = vegreview.objects.create(product_id=product_id,product_name=product_name,costamor_nam=costamor_nam,
            review=reviews) 
            rev.save();
            
            
            rev = vegreview.objects.filter(product_id=product_id)
            
            
               
        return redirect('/vegitable/detail/?product='+ pro_id)   


def autocom(request):
    
    if 'term' in request.GET:
        nam = request.GET['term']
        print(nam)
        name1 = list()
        food = vegitable.objects.filter(Q(name__istartswith=nam))
        for vegita in food:
            name1.append(vegita.name)
            print(name1)
        return JsonResponse(name1, safe=False) 
        
        
        
          
        
        
    food = vegitable.objects.all()
    return render(request, 'shop.html',{'food':food, 'qty':count1, 'cata':' VEGITABLE ', 'act2':'active', 'typ':typ})



