from django.db import models

# Create your models here.



class vegitable(models.Model):
   
    name = models.CharField(max_length= 150)
    quanty = models.FloatField(blank=True, null=True)
    date = models.DateField(null=True)
    img = models.ImageField(upload_to = 'froot', null=True, blank=True)
    img2 = models.ImageField(upload_to = 'froot',blank=True, null=True)
    img3 = models.ImageField(upload_to = 'froot', blank=True, null=True)
    price = models.FloatField(default=0.00)
    pakking = models.FloatField(blank=True, default=0.00)
    discount = models.FloatField(blank=True, null=True)
    tax = models.FloatField(blank=True, default=0, help_text='Enter the persatage of tax')
    offer = models.BooleanField(default=False)
    des = models.TextField(blank=True, null=True)