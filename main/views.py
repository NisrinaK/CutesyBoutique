from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()  # Mengambil semua produk dari database
    return render(request, 'main/product_list.html', {'products': products})

def show_info(request):
    return render(request, 'main/info.html')
