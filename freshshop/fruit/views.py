
from django.dispatch.dispatcher import receiver
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

def froot(request):
    typ = 'fruit'
   
    food = fruits.objects.all()
    return render(request, 'shop.html',{'food':food, 'qty':count2, 'cata':cata2, 'act1':'active','typ':typ})

def fdetail(request):
    typ = 'fruit'
    val = request.GET['product']
    obj = fruits.objects.get(id=val)
    rev = frureview.objects.filter(product_id=obj)
    food2 = fruits.objects.all()
    return render(request, 'shop-detail.html',{'obj':obj,'food':food2, 'rev':rev,'typ':typ})

    
    
        
        
        

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
        


        


    


       