"""
URL configuration for CutesyBoutique project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from main import views  # Import views from the 'main' app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', views.show_info, name='show_info'),
    path('products/', views.product_list, name='product_list'),
    path('', views.home, name='home'),  # Add this line to handle the empty path
]