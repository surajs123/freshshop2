from  django.urls import path
from .import views
from custamor.views import cartfun
urlpatterns = [
    path('', views.froot, name= 'froot'),
    path('detail/', views.fdetail, name='detail' ),
    path('detail/review/', views.frview, name='review'),
    path('cart/', cartfun, name='cart'),

]