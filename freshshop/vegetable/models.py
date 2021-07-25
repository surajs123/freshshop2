from django.db import models

# Create your models here.



class vegitable(models.Model):
   
    name = models.CharField(max_length= 150)
    quanty = models.FloatField(blank=True, null=True)
    date = models.DateField(null=True)
    img = models.ImageField(upload_to = 'froot', null=True, blank=True)
    img2 = models.ImageField(upload_to = 'froot',blank=True, null=True)
    img3 = models.ImageField(upload_to = 'froot', blank=True, null=True)
    droup = models.FloatField(blank=True, null=True)
    price = models.FloatField()
    offer = models.BooleanField(default=False)
    des = models.TextField(blank=True, null=True)