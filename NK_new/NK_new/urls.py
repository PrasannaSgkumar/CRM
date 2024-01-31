"""
URL configuration for NK_new project.

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
from django.http import HttpResponse
from New_app1 import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('dash/', views.dashboard, name='dash'),

    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customers/<str:pk>/', views.customers, name="customers"),
    path('dashboard', views.dashboard),
    path('create_order/<str:pk>/', views.create_order, name="create_order"),
    path('update_order/<str:pk>/', views.update_order, name="update_order"),
    path('delete_order/<str:pk>/', views.delete_order, name="delete_order"),
    path('create_customer/', views.create_customer, name="create_customer"),
    path('create_product', views.product_create, name='create_product'),
    path('delete_product/<str:pk>/', views.delete_product, name="delete_product"),
    # path('about/', views.contact),
    # path('products/', views.products),
    # path('customer/', views.customer),
]
