from  django.urls import path 
from .import views
urlpatterns = [
    path('', views.myaccount, name= 'account'),
    path('register/', views.regist, name='register'),
    path('login/', views.logina, name='login'),
    path('logout/', views.logouta, name='logout'),
    path('carten/', views.cartfun, name='carten'),
    path('cartdelect/', views.delectcart, name= 'cartdelect'),
    
    
    
]