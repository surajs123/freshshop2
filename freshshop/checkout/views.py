from django.shortcuts import render
from fruit.models import fruits
from vegetable.models import vegitable

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



