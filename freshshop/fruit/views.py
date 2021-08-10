
from django.db.models.query_utils import Q
from django.dispatch.dispatcher import receiver
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .models import fruits, frureview
from django.contrib.auth import authenticate
from django.contrib import messages
from custamor.models import onlineuser, CartModelFruite, CartModelvegitable
# Create your views here.
qtyf = fruits.objects.all()
count2 =0
cata2 = ' FRUITS '
for totf in qtyf:
    count2 =count2+totf.quanty
typ = 'fruit'
def froot(request):
    # this will count the number of cart in user saved
    count= 0
    if request.user.is_authenticated:
        login_user= request.user
        user_now= onlineuser.objects.get(id=login_user.id)
        count1 = CartModelFruite.objects.filter(costamor=user_now).count()
        count3 = CartModelvegitable.objects.filter(costamor=user_now).count()
        count = count1+count3

    if request.method == 'POST':
        value = request.POST['search']
        obj = fruits.objects.get(name=value)

       
        return render(request, 'shop.html',{'food':obj, 'qty':count2, 'cata':cata2, 'act1':'active','typ':typ, 'count':count})

    else:
        food = fruits.objects.all()
        return render(request, 'shop.html',{'food':food, 'qty':count2, 'cata':cata2, 'act1':'active','typ':typ,'count':count,'num':1})

def fdetail(request):
    # this will count the number of cart in user saved
    count= 0
    if request.user.is_authenticated:
        login_user= request.user
        user_now= onlineuser.objects.get(id=login_user.id)
        count1 = CartModelFruite.objects.filter(costamor=user_now).count()
        count3 = CartModelvegitable.objects.filter(costamor=user_now).count()
        count = count1+count3
    
    val = request.GET['product']
    obj = fruits.objects.get(id=val)
    rev = frureview.objects.filter(product_id=obj)
    food2 = fruits.objects.all()
    
    # this will find the actual price for the product 
    
    
    
    

    return render(request, 'shop-detail.html',{'obj':obj,'food':food2, 'rev':rev,'typ':typ,'count':count})

    
    
        
        
        

def frview(request):
    if request.method == 'POST':
        reviews = request.POST['review']
        pro_id =  request.POST['product']

        
        
       
        
        if reviews =="":
            print ('pleses enter the value ...')
        else:
            
            print ('poda patty')
            costamor_nam = request.POST['cos_name']
            obj = fruits.objects.get(id = pro_id)
            product_id = obj
            product_name = obj.name
            rev = frureview.objects.create(product_id=product_id,product_name=product_name,costamor_nam=costamor_nam,
            review=reviews) 
            rev.save();
            
            
            rev = frureview.objects.filter(product_id=product_id)
            
            
               
        return redirect('/fruit/detail/?product='+ pro_id)
        

def autocom(request):
    
    if 'term' in request.GET:
        nam = request.GET['term']
        print(nam)
        name1 = list()
        food = fruits.objects.filter(Q(name__istartswith=nam))
        for fruit in food:
            name1.append(fruit.name)
            print(name1)
        return JsonResponse(name1, safe=False) 
        
        
        
          
        
        
    food = fruits.objects.all()
    return render(request, 'shop.html',{'food':food, 'qty':count2, 'cata':cata2, 'act1':'active','typ':typ})




        
        


        


    


       