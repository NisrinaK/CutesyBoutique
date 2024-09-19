from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

def show_info(request):
    return render(request, 'main/info.html')

def home(request):
    return render(request, 'main/home.html')

# Menambah Produk
def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save() #form.save()
        return redirect("main:show_home")

    context = {'form': form}
    return render(request, "add_product.html", context) #'main/add_product.html'

@login_required(login_url='/login')
def show_home(request):
    products = Product.objects.filter(user=request.user) #products = Product.objects.all()
    context = {
        'barang' : '2323061456',
        'descripsion': 'Pak Bepe',
        'size': 'PBP E',
        'price': 'PBP E',
        'stock': 'PBP E',
        'products' : products,
        'last_login': request.COOKIES.get('last_login'),
        'name': request.user.username,
    }

    return render(request, "home.html", context) #(request, 'main/home.html', context)

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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_home"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))  # Mengarahkan kembali ke halaman login setelah logout
    response.delete_cookie('last_login')  # Menghapus cookie last_login
    return response