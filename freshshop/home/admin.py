from django.contrib import admin
from .import models
import home
# Register your models here.


class HomeAdmin(admin.AdminSite):
    site_header = 'Home Admin Database'



home_site = HomeAdmin(name='HomeAdmin')

home_site.register(models.TitleOffer)
home_site.register(models.Advertise)
home_site.register(models.Blog)