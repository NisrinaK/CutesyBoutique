from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', views.show_info, name='show_info'),
    path('products/', views.product_list, name='product_list'),
    path('', views.home, name='home'),
    path('add-product/', views.add_product, name='add_product'),
    path('products/xml/', views.product_xml, name='product_xml'),
    path('products/xml/<int:id>/', views.product_xml_by_id, name='product_xml_by_id'),
    path('products/json/', views.product_json, name='product_json'),
    path('products/json/<int:id>/', views.product_json_by_id, name='product_json_by_id'),
]
