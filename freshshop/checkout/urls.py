from  django.urls import path
from .import views

urlpatterns = [
    path('', views.checkhome, name= 'checkout'),
    path('order/', views.order, name= 'order-summery'),
    path('biladdress<int:id>/', views.biladdress,name='bil_address'),
    path('edit<int:id>/', views.edit ,name='editaddress'),
    path('remove<int:id><int:user>/', views.address_remove, name='removeaddress'),

]