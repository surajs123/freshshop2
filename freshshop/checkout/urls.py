from  django.urls import path
from .import views

urlpatterns = [
    path('', views.checkhome, name= 'checkout'),
    path('order/', views.order, name= 'order-summery'),
    path('biladdress<str:typ>/', views.biladdress,name='bil_address'),
    path('edit<str:typ>/', views.edit ,name='editaddress'),
    path('remove<str:typ>/', views.address_remove, name='removeaddress'),
    path('billselect<str:typ>/', views.selectaddress, name='bilselect'),
    path('billaddget/',views.getbilladdress, name='getbill_address'),


]