from django.contrib import admin
from .import models
# Register your models here.

class ShopAdminArea(admin.AdminSite):
    site_header = 'Vegitable Database'

vegitable_site = ShopAdminArea(name='VegitableAdmin')

vegitable_site.register(models.vegitable)
 