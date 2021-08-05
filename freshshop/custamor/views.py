
from django.contrib import auth
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import  onlineuser, CartModelFruite, CartModelvegitable
from django.contrib import messages
import time
from fruit.models import fruits
from vegetable.models import vegitable
# Create your views here.


def myaccount(request):
    return render(request, 'wishlist.html')

def regist(request):
    
    if request.method == 'POST':
        email=request.POST['email']
        user_name=request.POST['user_name']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        gender=request.POST['gender']
        address=request.POST['address']
        place=request.POST['place']
        pincode=request.POST['pincode']
        password=request.POST['password']
        password2=request.POST['password2']

        

        if email != '' and user_name != '':
            
            if password==password2:

                if onlineuser.objects.filter(email=email).exists():
                    messages.warning(request,' This email was alredy Teken..')
                    return redirect('register') 
                    
                   

                else:    
                    user = onlineuser.objects.create_user(email=email,user_name=user_name,first_name=first_name, last_name=last_name,gender=gender,address=address,
                    place=place,pincode=pincode,password=password, is_active=True)
                    user.save();
                    messages.success(request, " User is Success fully Created..! ")
                    auth.login(request,user)
                    
                    
            else:
                data=dict()
                messages.error(request, " The password not mach")
                return redirect('register')
        else:
            messages.warning(request, " please fill the fields ") 
            return redirect('register')
        
        return redirect('/')      

    else:

        return render(request, 'register.html')  



def logina(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")

        else:
            return render(request, 'login.html')
    


    else:
        return render(request, 'login.html')


def logouta(request):
    
    auth.logout(request)
    return redirect('/')


def cartfun(request):
    if request.method=='POST':
       obj_id = request.POST['froot']
       cos = request.POST['costa']
       typeof = request.POST['typin']
       
       if typeof == 'fruit':
           obj_th1 = fruits.objects.get(id=obj_id)
           costa = onlineuser.objects.get(id=cos)
           if CartModelFruite.objects.filter(product=obj_th1).exists():
               print("alredy add this  product")

           else:
              obj_fr = CartModelFruite.objects.create(costamor=costa, product=obj_th1)
              obj_fr.save();

           cart_ve = CartModelvegitable.objects.filter(costamor=costa)
           cart_fr = CartModelFruite.objects.filter(costamor=costa)
           return render(request, 'cart.html', {'cart_fr':cart_fr, 'cart_ve':cart_ve} )
       if typeof == 'vegita':
            obj_th2 = vegitable.objects.get(id=obj_id)
            costa = onlineuser.objects.get(id=cos)
            if CartModelvegitable.objects.filter(product=obj_th2).exists():
               print("alredy add this  product")
            else:   
                obj_ve = CartModelvegitable.objects.create(costamor=costa, product=obj_th2)
                obj_ve.save();

            cart_ve = CartModelvegitable.objects.filter(costamor=costa)
            cart_fr = CartModelFruite.objects.filter(costamor=costa)
            return render(request, 'cart.html', {'cart_ve':cart_ve, 'cart_fr':cart_fr})

       else:
            print('thos will not work')    
                  


       

    else:
        cos = request.GET['cos_id']
        cos_obj = onlineuser.objects.get(id=cos)

        cart_ve = CartModelvegitable.objects.filter(costamor=cos_obj)
        cart_fr = CartModelFruite.objects.filter(costamor=cos_obj)
        return render(request, 'cart.html', {'cart_ve':cart_ve, 'cart_fr':cart_fr})

# to delete the cart object 


def delectcart(request):
    typ = request.GET['type']
    if typ == 'fruit':

        cos_id = request.GET['cos']
        deli = request.GET['deli']
        CartModelFruite.objects.get(id=deli).delete()
    if typ == 'vegita':

        cos_id = request.GET['cos']
        deli = request.GET['deli']
        CartModelvegitable.objects.get(id=deli).delete()

    else:
        print("somthing wrong in delete cart... ")    
            
    return redirect('/account/carten/?cos_id='+cos_id)



