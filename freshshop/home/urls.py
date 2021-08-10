from  django.urls import path 
from .import views
urlpatterns = [
    path('', views.index, name= 'index'),
    path('<int:id>/', views.update_user, name='update_user'),
    path('surchvalue/', views.surch, name='surchvalue')
    
    
    
]