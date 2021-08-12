from django.contrib.auth.models import User
from custamor.models import onlineuser
from django.shortcuts import render
from fruit.models import fruits
from vegetable.models import vegitable
from .import models 

# Create your views here.

def checkhome(request):
    if request.method == 'GET':
        obj_id = request.GET['froot']
        user_id = request.GET['costa']
        qty = request.GET['qty']
        if request.GET['typin'] == 'fruit':
            obj = fruits.objects.get(id=obj_id)
        else:
            obj = vegitable.objects.get(id=obj_id) 

        print(obj) 


        
        item_price = obj.price * float(qty)
        pakking = 50
        discount = obj.droup
        sub_total = (item_price + pakking) - discount
        tax = sub_total * 0.16
        round(tax, 2)

        # to remove the decimal part of total amout and it will add to item_price for taly

        tax1 = int(tax + 1.00)

        tax2 = float(tax1)-tax
        print(tax1)
        round(tax2, 2)
        print(tax2)

        total = sub_total + tax
        

        checkout = [item_price, pakking, discount, sub_total,tax, total, qty]

        print (checkout)
    

        





    return render (request, 'checkout.html', {'checkout':checkout})




def order(request):
 return render(request, 'order-summery.html')   


def biladdress(request,id):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        country = request.POST['country']
        state = request.POST['state']
        email = request.POST['email']
        district = request.POST['district']
        phone_no1 = request.POST['phone1']
        phone_no2 = request.POST['phone2']
        pincode = request.POST['pin']
        if state == '' or district == '' or country == '':
            state_m=True
            district_m = True
            country_m = True
            msg=[state_m,district_m,country_m]
            cout = models.Checkoutaddress.objects.filter(user_id=id)
            return render(request, 'billig-address.html', {'cout':cout,'msg':msg})



        if first_name !='' and last_name !='' and address1 !='' and phone_no1 !='' and pincode !='' and state !='' and district !='' and country !='':
            if phone_no2 == '':
                phone_no2 = 0
            user_id = onlineuser.objects.get(id=id)
            obj = models.Checkoutaddress.objects.create(email=email,user_id=user_id,first_name=first_name,last_name=last_name,address1=address1,address2=address2,contry=country,state=state,district=district,phone_no1=phone_no1,phone_no2=phone_no2,pincode=pincode)
            obj.save();

        return render(request, 'checkout.html')

    else:
        cout = models.Checkoutaddress.objects.filter(user_id=id)
        return render(request, 'billig-address.html', {'cout':cout})

def edit(request,id):
    
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        country = request.POST['country']
        state = request.POST['state']
        user_id = request.POST['user']
        district = request.POST['district']
        phone_no1 = request.POST['phone1']
        phone_no2 = request.POST['phone2']
        pincode = request.POST['pin']
        if state == '' or district == '' or country == '':
            state_m=True
            district_m = True
            country_m = True
            msg=[state_m,district_m,country_m]
            bill = models.Checkoutaddress.objects.get(id=id)
            return render(request, 'billig-address-edit.html', {'bill':bill})



        if first_name !='' and last_name !='' and address1 !='' and phone_no1 !='' and pincode !='' and state !='' and district !='' and country !='':
            if phone_no2 == '':
                phone_no2 = 0
            
            models.Checkoutaddress.objects.filter(id=id).update(first_name=first_name,last_name=last_name,address1=address1,address2=address2,contry=country,state=state,district=district,phone_no1=phone_no1,phone_no2=phone_no2,pincode=pincode)
            cout = models.Checkoutaddress.objects.filter(user_id=user_id)
            return render(request, 'billig-address.html', {'cout':cout})


    else:
        bill = models.Checkoutaddress.objects.get(id=id)
        return render(request, 'billig-address-edit.html', {'bill':bill})


    
def address_remove(request,id,user):
    models.Checkoutaddress.objects.get(id=id).delete()
    usr = models.onlineuser.objects.get(id=user)
    obj = models.Checkoutaddress.objects.filter(user_id=usr)

    return render(request, 'billig-address.html', {'cout':obj})





