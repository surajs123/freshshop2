"""freshshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from fruit.admin import fruit_site
from home.admin import home_site
from django.conf import settings
from vegetable.admin import vegitable_site
from checkout.admin import checkout_site
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    path('fruit/', include('fruit.urls')),
    path('vegitable/', include('vegetable.urls')),
    path('admin/', admin.site.urls),
    path('fruitadmin/', fruit_site.urls),
    path('vegitableadmin/', vegitable_site.urls),
    path('homeadmin/', home_site.urls),
    path('Checkoutadmin/', checkout_site.urls),
    path('account/', include('custamor.urls')),
    path('checkout/', include('checkout.urls')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


