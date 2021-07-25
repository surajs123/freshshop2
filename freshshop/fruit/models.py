
import functools
from django.db import models
from django.utils import timezone

# Create your models here.
class fruits(models.Model):
   
    name = models.CharField(max_length= 150)
    quanty = models.FloatField(null=True, blank=True)
    date = models.DateField(null=True,blank=True)
    img = models.ImageField(upload_to = 'froot', null=True, blank=True)
    img2 = models.ImageField(upload_to = 'froot',blank=True, null=True)
    img3 = models.ImageField(upload_to = 'froot',blank=True, null=True)
    droup = models.FloatField(blank=True, null=True)
    price = models.FloatField()
    offer = models.BooleanField(default=False)
    des = models.TextField(blank=True, null=True)