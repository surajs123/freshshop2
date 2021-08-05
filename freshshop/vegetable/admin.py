from django.contrib import admin
from .import models
import vegetable
from django.forms import Textarea
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class ShopAdminArea(admin.AdminSite):
    site_header = 'Vegitable Database'

    
    
class VegAdminConfig (admin.ModelAdmin):
    search_fields = ('name','date',)
    list_display = ('name','quanty','price','discount','offer')
    ordering = ('-date',)
    list_filter = ('name','date','offer')

    fieldsets = (
        (None, {'fields':('name', 'date', 'quanty',)}),
        ('pricingFields', {'fields':('price','pakking','discount','tax',)}),
        ('ImageFields', {'fields':('img','img2','img3')}),
        ('Offer and dis', {'fields':('offer','des')}),
    )
    formfield_overrides = {
        models.vegitable.des:{'widget': Textarea(attrs={'rows':30, 'cols':40})},
    }
    add_fieldsets =(
        (None,{
            'classes': ('wide',),
            'fields': ('name', 'date', 'quanty','img1','img2','img3','price','pakking','discount','tax','offer','dis')
        }),
    )
   





vegitable_site = ShopAdminArea(name='VegitableAdmin')

vegitable_site.register(models.vegitable, VegAdminConfig)




