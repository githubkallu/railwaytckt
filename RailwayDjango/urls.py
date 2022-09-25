"""RailwayDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from railway.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',nav,name="nav"),
    path('login/',Login_customer,name="login_customer"),
    path('register_customer/',Register_customer,name="register_customer"), 
    path('search_train/',Search_Train,name="search_train"), 
    path('dashboard/',Dashboard,name="dashboard"),  
    path('log_out/',Logout,name="log_out"),
    path('book_detail/(?P<coun>[0-9]+)/(?P<pid>[0-9]+)/(<str:route1>)',Book_detail,name="book_detail"),
    path('addtrain/', Add_train, name="add_train"),
    path('addroute/', add_route, name="add_route"),   
    path('viewtrain/', view_train, name="view_train"),   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
