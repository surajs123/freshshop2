from django.db import models
from django.utils import timezone

# Create your models here.



class vegitable(models.Model):
   
    name = models.CharField(max_length= 150)
    quanty = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to = 'froot', null=True, blank=True)
    img2 = models.ImageField(upload_to = 'froot',blank=True, null=True)
    img3 = models.ImageField(upload_to = 'froot', blank=True, null=True)
    price = models.FloatField(default=0.00)
    pakking = models.FloatField(blank=True, default=0.00)
    discount = models.FloatField(blank=True,)
    tax = models.FloatField(blank=True, default=0, help_text='Enter the persatage of tax')
    offer = models.BooleanField(default=False)
    des = models.TextField(blank=True, null=True)
    

    @property
    def net_price(self):
        tax =  self.price * (self.tax /100)
        price = (self.price - self.discount) + tax + self.pakking
        return price

    # this for checkout the value without discount named as droup

    @property
    def droup(self):
        droup = self.net_price + self.discount
        return droup

    @property
    def tax1(self):
        tax = self.price*(self.tax/100)
        return tax

    def __str__(self):
        return self.name


# create a review

class vegreview(models.Model):
    product_id = models.ForeignKey(vegitable, on_delete= models.CASCADE)
    costamor_nam = models.CharField(max_length=100, blank=True)
    product_name = models.CharField(max_length=100,blank=True)
    review_date = models.DateTimeField(default=timezone.now)
    review = models.TextField(max_length=400)
