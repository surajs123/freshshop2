from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import onlineuser, CartModelvegitable, CartModelFruite
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea, TextInput
# Register your models here.


class UserAdminConfig(UserAdmin):
    search_fields = ('email','user_name','first_name',)
    list_filter = ('email','user_name','first_name','is_active','is_staff')
    ordering = ('-start_date',)
    list_display = ('email','user_name','first_name','is_active','is_staff')

    fieldsets = (
        (None, {'fields':('email', 'user_name', 'first_name',)}),
        ('personal', {'fields':('gender','address', 'place','pincode',)}),
        ('Permissions', {'fields':( 'user_permissions','is_active','password')}),
        ('SpecialPermissions',{'fields':('is_staff','is_superuser')}),
       
    )

    



    formfield_overrides = {
        onlineuser.address:{'widget': Textarea(attrs={'rows':30, 'cols':40})},
    }
    add_fieldsets =(
        (None,{
            'classes': ('wide',),
            'fields': ('email','user_name','first_name','password1','password2','is_active','is_staff')
        }),
    )
    


       


admin.site.register(onlineuser, UserAdminConfig)
admin.site.register(CartModelvegitable)
admin.site.register(CartModelFruite)