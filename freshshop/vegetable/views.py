from django.shortcuts import render, redirect
from .models import vegitable, vegreview
# Create your views here.
qtyv = vegitable.objects.all()
count1 =0

for totv in qtyv:
    count1 =count1+totv.quanty


def vegi(request):
    typ = 'vegita'
   
    food = vegitable.objects.all()
    return render(request, 'shop.html',{'food':food, 'qty':count1, 'cata':' VEGITABLE ', 'act2':'active', 'typ':typ})

def vdetail(request):
    typ = 'fruit'
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