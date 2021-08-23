from  django.urls import path
from .import views

urlpatterns = [
    path('', views.checkhome, name= 'checkout'),
    path('order/', views.order, name= 'order-summery'),
    path('biladdress<int:id><str:typ><int:obj><int:qty>/', views.biladdress,name='bil_address'),
    path('edit<int:id><int:user><str:typ><int:obj><int:qty>/', views.edit ,name='editaddress'),
    path('remove<int:id><int:user><str:typ><int:obj><int:qty>/', views.address_remove, name='removeaddress'),
    path('billselect<int:id><str:typ><int:obj><int:qty>/', views.selectaddress, name='bilselect'),
    path('billaddget<int:id>/',views.getbilladdress, name='getbill_address')

]