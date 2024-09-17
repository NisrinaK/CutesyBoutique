from django.contrib import admin
from django.urls import path
from . import views
from main.views import add_product
from main.views import show_home
app_name = 'main'

#urls path
urlpatterns = [
    path('', show_home, name='show_home'),
    path('add_product/', add_product, name='add_product'),
    path('products/xml/', views.product_xml, name='product_xml'), #XML
    path('products/xml/<int:id>/', views.product_xml_by_id, name='product_xml_by_id'),
    path('products/json/', views.product_json, name='product_json'), #JSON
    path('products/json/<int:id>/', views.product_json_by_id, name='product_json_by_id'),
]
