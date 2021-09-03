from  django.urls import path 
from .import views
urlpatterns = [
    path('', views.index, name= 'index'),
    path('user_update/', views.update_user, name='update_user'),
    
    
    
    
]