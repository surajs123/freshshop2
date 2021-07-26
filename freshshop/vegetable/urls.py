from  django.urls import path 
from .import views
from custamor.views import cartfun
urlpatterns = [
    path('', views.vegi, name= 'vegi'),
    path('detail/', views.vdetail ),
    path('detail/review/', views.vegview, name='review'),
    path('cart/', cartfun, name='cart'),
    path('review/', views.vegview, name='review'),
]