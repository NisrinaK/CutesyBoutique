from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.http import HttpResponse
from django.core import serializers

def show_info(request):
    return render(request, 'main/info.html')

def home(request):
    return render(request, 'main/home.html')

# Menambah Produk
def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_home")

    context = {'form': form}
    return render(request, "add_product.html", context)

def show_home(request):
    products = Product.objects.all()
    context = {
        'barang' : '2323061456',
        'descripsion': 'Pak Bepe',
        'size': 'PBP E',
        'price': 'PBP E',
        'stock': 'PBP E',
        'products' : products,
    }

    return render(request, "home.html", context)

# XML

def show_xml(request):
    product = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", product), content_type="application/xml")

def show_xml_by_id(request, id):
    product = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", product), content_type="application/xml")

# JSON
def show_json(request):
    product = Product.objects.all()
    return HttpResponse(serializers.serialize("json", product), content_type="application/json")

def show_json_by_id(request, id):
    product = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", product), content_type="application/json")
