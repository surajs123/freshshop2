from django.contrib import admin
from .import models
# Register your models here.
class CheckAdminArea(admin.AdminSite):
    site_header = 'Checkout Database'

checkout_site = CheckAdminArea(name='checktableAdmin')
checkout_site.register(models.Checkoutaddress)
checkout_site.register(models.Checkout)