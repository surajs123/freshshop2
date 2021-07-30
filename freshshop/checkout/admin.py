from django.contrib import admin
from .import models
# Register your models here.


class ShopAdminArea(admin.AdminSite):
    site_header = 'checkout Database'

checkout_site = ShopAdminArea(name='CheckoutAdmin')
checkout_site.register(models.Checkout)
checkout_site.register(models.Checkoutaddress)



