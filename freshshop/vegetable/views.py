from django.shortcuts import render
from .models import vegitable
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
    val = request.GET['product']
    obj = vegitable.objects.get(id=val)
    food2 = vegitable.objects.all()
    return render(request, 'shop-detail.html',{'obj':obj,'food':food2})      