from django.contrib import admin
from .import models
from django.forms import Textarea

# Register your models here.

class ShopAdminArea(admin.AdminSite):
    site_header = 'Fruit Database'


class FruitAdminConfig (admin.ModelAdmin):
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
        models.fruits.des:{'widget': Textarea(attrs={'rows':30, 'cols':40})},
    }
    add_fieldsets =(
        (None,{
            'classes': ('wide',),
            'fields': ('name', 'date', 'quanty','img1','img2','img3','price','pakking','discount','tax','offer','dis')
        }),
    )


fruit_site = ShopAdminArea(name='FruitAdmin')
fruit_site.register(models.fruits, FruitAdminConfig)


 