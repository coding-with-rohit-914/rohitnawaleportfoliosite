"""
URL configuration for portfolioproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from portfolioapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('RohitPage', views.RohitPage, name='Rohit'),
    path('index', views.index, name='index'),
    path('About', views.AboutPage, name='About'),
    path('MyWork', views.MyWorkPage, name='MyWork'),
    path('Services', views.ServicesPage, name='Services'),
    path('Contact', views.ContactPage, name='Contact'),
    path('Feedback', views.Feedback, name='Feedback')
]
