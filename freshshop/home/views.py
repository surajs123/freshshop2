from django.contrib.auth import login
from django.db.models.query_utils import Q
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from custamor.models import onlineuser, CartModelFruite, CartModelvegitable
from fruit.models import fruits
from django.contrib import messages
from vegetable.models import vegitable

# Create your views here.

def index(request):
    # this will count the number of cart in user saved
    count= 0
    if request.user.is_authenticated:
        login_user= request.user
        user_now= onlineuser.objects.get(id=login_user.id)
        count1 = CartModelFruite.objects.filter(costamor=user_now).count()
        count2 = CartModelvegitable.objects.filter(costamor=user_now).count()
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



def update_user(request,id):
    
    if request.method == 'POST':
        
        user_name=request.POST['user_name']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        gender=request.POST['gender']
        address=request.POST['address']
        place=request.POST['place']
        pincode=request.POST['pincode']
        

        

        if  user_name != '':
            
            onlineuser.objects.filter(id=id).update(user_name=user_name,first_name=first_name, last_name=last_name,gender=gender,address=address,
            place=place,pincode=pincode, is_active=True)

            print('the user updated  ')
            
            
            
            
            
                    
                    
            
        else:
            messages.warning(request, " please fill the fields ") 
            return redirect('updateuser')
        
        return redirect('/')      

    else:

        user = onlineuser.objects.get(id=id)

        return render(request, 'register-update.html',{'userd':user})  

        







