from django.urls import path
from main.views import add_product, show_json, show_json_by_id, show_xml, show_xml_by_id, add_product_ajax
from main.views import show_home
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_product
from main.views import delete_product
app_name = 'main'

urlpatterns = [
    path('', show_home, name='show_home'),
    path('add_product/', add_product, name='add_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<str:id>/', edit_product, name='edit_product'),
    path('delete/<str:id>/', delete_product, name='delete_product'),
    path('create/product/ajax/', add_product_ajax, name='add_product_ajax'),
]
