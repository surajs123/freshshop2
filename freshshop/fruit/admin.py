from django.contrib import admin
from .import models


# Register your models here.

class ShopAdminArea(admin.AdminSite):
    site_header = 'Fruit Database'

fruit_site = ShopAdminArea(name='FruitAdmin')
fruit_site.register(models.fruits)


 