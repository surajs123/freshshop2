from  django.urls import path 
from .import views
from custamor.views import cartfun
urlpatterns = [
    path('', views.vegi, name= 'vegi'),
    path('detail/', views.vdetail ),
    path('cart/', cartfun, name='cart'),
]