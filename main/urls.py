from django.contrib import admin
from django.urls import path
from . import views
from main.views import add_product, show_json, show_json_by_id, show_xml, show_xml_by_id
from main.views import show_home
from main.views import register
from main.views import login_user
from main.views import logout_user
app_name = 'main'

#urls path oke
urlpatterns = [
    path('', show_home, name='show_home'),
    path('add_product/', add_product, name='add_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
