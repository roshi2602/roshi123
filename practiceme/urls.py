"""practiceme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
#from django.conf.urls import path
from django.conf import settings
from appatt.views import ( index, user_login, user_logout,
    success, ProfileUpdate, MyProfile)

#from apphi.views import Product_Createview
urlpatterns = [

    path('admin/', admin.site.urls),
    #path('we/', views.Product_Createview.as_view()),
    #product('go/', views.Product_Formview.as_view()),
    path('employee/', include('appatt.urls')),
    path('login/', user_login, name="user_login"),
    path('success/', success, name="user_success"),
    path('logout/', user_logout, name="user_logout"),
    path('profile/', MyProfile.as_view(), name="my_profile"),
    path('profile/update', ProfileUpdate.as_view(), name="update_profile"),
    









    ]