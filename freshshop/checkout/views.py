from django.contrib.auth.models import User
from custamor.models import onlineuser
from django.shortcuts import render
from fruit.models import fruits
from vegetable.models import vegitable
from .import models 

# Create your views here.

def checkhome(request):
    
 return render (request, 'checkout.html',)




def order(request):
 return render(request, 'order-summery.html') 

def getbilladdress(request):
    id = request.GET['user']
    typ = request.GET['typ']
    obj = request.GET['obj']
    qty = request.GET['qty']

    cout = models.Checkoutaddress.objects.filter(user_id=id)
    return render(request, 'billig-address.html',{'typ':typ, 'obj':obj,'cout':cout,'qty':qty})



def biladdress(request,typ):

    if request.method == 'POST':
        id = request.POST['user']
        obj = request.POST['obj']
        qty = request.POST['qty']
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
            obje = models.Checkoutaddress.objects.create(email=email,user_id=user_id,first_name=first_name,last_name=last_name,address1=address1,address2=address2,contry=country,state=state,district=district,phone_no1=phone_no1,phone_no2=phone_no2,pincode=pincode)
            obje.save();


            # if the address was created the data will got the next step checkout 

            if typ == 'fruit':
                objFW = fruits.objects.get(id=obj)
               

            if typ == 'vegita':
                objFW = vegitable.objects.get(id=obj)    


            priceU = objFW.price * qty
            taxU = objFW.tax1 * qty
            pakkingU = objFW.pakking * qty
            after_tax = priceU + taxU + pakkingU
            discountU = objFW.discount * qty
            grant_total = after_tax - discountU

        
            
            return render(request, 'checkout.html', {'typ':typ,'obj':objFW,'obja':obje,'qty':qty, 'price':priceU,'tax':taxU,'pakking':pakkingU,'aftertax':after_tax,'discount':discountU,'granttotal':grant_total})
        cout = models.Checkoutaddress.objects.filter(user_id=id)
        return render(request, 'billig-address.html', {'typ':typ, 'obj':obj, 'id':id, 'cout':cout,'qty':qty})

    else:
        cout = models.Checkoutaddress.objects.filter(user_id=id)
        return render(request, 'billig-address.html',{'typ':typ, 'obj':obj, 'id':id,'cout':cout,'qty':qty})

def edit(request,typ):
    
    if request.method == 'POST':
        id = request.POST['id']
        user = request.POST['user']
        obj = request.POST['obj']
        qty = request.POST['qty']
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
            return render(request, 'billig-address-edit.html', {'bill':bill,'typ':typ, 'obj':obj, 'id':user,'qty':qty})



        if first_name !='' and last_name !='' and address1 !='' and phone_no1 !='' and pincode !='' and state !='' and district !='' and country !='':
            if phone_no2 == '':
                phone_no2 = 0
            
            models.Checkoutaddress.objects.filter(id=id).update(first_name=first_name,last_name=last_name,address1=address1,address2=address2,contry=country,state=state,district=district,phone_no1=phone_no1,phone_no2=phone_no2,pincode=pincode)
            cout = models.Checkoutaddress.objects.filter(user_id=user_id)
            return render(request, 'billig-address.html', {'cout':cout,'typ':typ, 'obj':obj, 'id':user,'qty':qty})


    else:
        id = request.GET['id']
        user = request.GET['user']
        obj = request.GET['obj']
        qty = request.GET['qty']
        bill = models.Checkoutaddress.objects.get(id=id)
        return render(request, 'billig-address-edit.html', {'bill':bill,'typ':typ, 'obj':obj, 'id':user,'qty':qty})


    
def address_remove(request,typ):
    id = request.GET['id']
    user = request.GET['user']
    obj = request.GET['obj']
    qty = request.GET['qty']

    models.Checkoutaddress.objects.get(id=id).delete()
    usr = models.onlineuser.objects.get(id=user)
    obj = models.Checkoutaddress.objects.filter(user_id=usr)

    return render(request, 'billig-address.html', {'cout':obj,'typ':typ, 'obj':obj, 'id':user,'qty':qty})


def selectaddress(request,typ):
    id = request.GET['id']
    obj = request.GET['obj']
    qty = request.GET['qty']
    
    obja= models.Checkoutaddress.objects.get(id=id)
    if typ == 'fruit':
        objFW = fruits.objects.get(id=obj)

    if typ == 'vegita':
        objFW = vegitable.objects.get(id=obj)
    qty= int(qty)
    priceU = objFW.price * qty
    taxU = objFW.tax1 * qty
    taxU = round (taxU, 2)
    pakkingU = objFW.pakking * qty
    after_tax = priceU + taxU + pakkingU
    discountU = objFW.discount * qty
    grant_total = after_tax - discountU
    grant_total = round(grant_total, 2)
     
    print(  'the price is = ', priceU)     
    return render(request, 'checkout.html', {'typ':typ,'obj':objFW,'obja':obja, 'qty':qty, 'price':priceU,'tax':taxU,'pakking':pakkingU,'aftertax':after_tax,'discount':discountU,'granttotal':grant_total})

   

