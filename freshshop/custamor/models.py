
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager,User
from django.db.models.fields import BooleanField
from django.utils import timezone

# Create your models here.


class NewUser(BaseUserManager):
    def create_superuser(self, email, user_name, password, first_name,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_superuser') is not True:
            raise ValueError('superusr must be assigned to is_superuser=True')
        return self.create_user(email, user_name,first_name, password, **other_fields) 
    def create_user(self, email, user_name,first_name, password, **other_fields):

        if not email:
            raise ValueError('you must provide an email address ')
        
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, password=password, **other_fields)
        user.set_password(password)
        user.save()
        return user

class onlineuser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True )
    user_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, blank=True, default=False)
    last_name = models.CharField(max_length=100, blank=True, default=False)
    start_date =models.DateTimeField(default=timezone.now)
    gender = models.CharField(max_length=100, blank=True, default=False)
    address = models.TextField(max_length=200, blank=True, default=False)
    place = models.CharField(max_length=100,blank=True, default=False)
    pincode = models.IntegerField(default=00, blank=True)
    is_staff = BooleanField(default=False)
    is_active = BooleanField(default=False )

    objects = NewUser()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.user_name