from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', views.show_info, name='show_info'),
    path('products/', views.product_list, name='product_list'),
    path('', views.home, name='home'), 
]
