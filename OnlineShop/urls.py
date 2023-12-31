"""
URL configuration for OnlineShop project.

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
from django.urls import path, include
from product.views import ProductList, ProducTypeList, ProductDetail, ProductTypeDetail, home


urlpatterns = [
    path('', home, name='home-page'),
    path('admin/', admin.site.urls),
    path('api/product/', ProductList.as_view(), name='products'),
    path('api/categories/', ProducTypeList.as_view(), name='product-type'),
    path('api/product/<int:pk>', ProductDetail.as_view(), name='product-detail'),
    path('api/categories/<int:pk>', ProductTypeDetail.as_view(), name='type-detail')
]


