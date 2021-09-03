from django.contrib.auth import login
from django.db.models.query_utils import Q
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from custamor.models import onlineuser, CartModelFruite, CartModelvegitable
from fruit.models import fruits
from django.contrib import messages
from vegetable.models import vegitable
from .import models
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
        
    offers = models.TitleOffer.objects.all()
    blogs = models.Blog.objects.all()
    advertise = models.Advertise.objects.all()
    return render (request, 'index.html',{'count':count, 'offers':offers,'blogs':blogs,'advertise':advertise} )



         



def update_user(request):
    id= request.GET['update_id']
    
    if request.method == 'POST':
        
        user_name=request.POST['user_name']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        gender=request.POST['gender']
        address=request.POST['address']
        place=request.POST['place']
        pincode=request.POST['pincode']
        

        

        if  user_name == '' or pincode =='':
            msg="Canot empty the username and pincode columns "
            color = 'warning'
            user = onlineuser.objects.get(id=id)

            return render(request, 'register-update.html',{'userd':user,'msg':msg,'colour':color}) 
        else:
            onlineuser.objects.filter(id=id).update(user_name=user_name,first_name=first_name, last_name=last_name,gender=gender,address=address,
            place=place,pincode=pincode, is_active=True)

            print('the user updated  ')
        
        return redirect('/')      

    else:

        user = onlineuser.objects.get(id=id)

        return render(request, 'register-update.html',{'userd':user})  

        







