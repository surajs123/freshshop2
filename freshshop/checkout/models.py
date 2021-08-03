from django.db import models

# Create your models here.
from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import DateTimeField
from django.utils import timezone


    
from custamor.models import onlineuser

# Create your models here.

class Checkoutaddress(models.Model):
    user_id = models.ForeignKey(onlineuser, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address1 = models.TextField(max_length=200)
    address2 = models.TextField(max_length=200)
    contry = models.CharField (max_length=150)
    state = models.CharField(max_length=150)
    district = models.CharField(max_length=150)
    pincode = models.IntegerField()




class Checkout(models.Model):
    
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    shipping_address = models.TextField(max_length=400)
    product_type = models.CharField(max_length=50)
    product_name = models.CharField(max_length=150)
    qty = models.FloatField(default=0)
    item_price = models.FloatField(default=0.00)
    pakking_cost = models.FloatField(default=0.00)
    dicount = models.FloatField(default=0.00)
    tax = models.FloatField(default=0.00)
    shipping_cost = models.FloatField(default=0.00)
    grant_total = models.FloatField(default=0.00)
    



