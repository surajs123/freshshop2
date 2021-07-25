from  django.urls import path
from .import views
from custamor.views import cartfun
urlpatterns = [
    path('', views.froot, name= 'froot'),
    path('detail/', views.fdetail, name='detail' ),
    path('review/', views.derew, name='review'),
    path('cart/', cartfun, name='cart'),

]