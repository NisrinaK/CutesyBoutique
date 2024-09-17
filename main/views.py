from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.http import HttpResponse
from django.core import serializers

def product_list(request):
    products = Product.objects.all()  # Mengambil semua produk dari database
    return render(request, 'main/product_list.html', {'products': products})

def show_info(request):
    return render(request, 'main/info.html')

def home(request):
    return render(request, 'main/home.html')

#Menambah Produk
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'main/add_product.html', {'form': form})

#XML
def product_xml(request):
    products = Product.objects.all()
    data = serializers.serialize('xml', products)
    return HttpResponse(data, content_type='application/xml')

def product_xml_by_id(request, id):
    product = Product.objects.filter(id=id)
    data = serializers.serialize('xml', product)
    return HttpResponse(data, content_type='application/xml')

#JSON
def product_json(request):
    products = Product.objects.all()
    data = serializers.serialize('json', products)
    return HttpResponse(data, content_type='application/json')

def product_json_by_id(request, id):
    product = Product.objects.filter(id=id)
    data = serializers.serialize('json', product)
    return HttpResponse(data, content_type='application/json')