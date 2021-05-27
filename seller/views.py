from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.shortcuts import render, redirect
from .models import Seller
from eshop.models import Product
from .forms import ProductForm
from django.utils.text import slugify
def become_seller(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('seller_dashboard')
            # user = form.save()

            # login(request, user)
            # seller = Seller.objects.create(name=user.username, created_by=user)
            

    else:
        form = UserRegisterForm()
    return render(request, 'become_seller.html',{'form':form})




@login_required
def seller_dashboard(request):
    seller = request.user.seller
    products = seller.products.all()
    return render(request, 'seller_dashboard.html',{'seller':seller, 'products':products})


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user.seller
            product.slug = slugify(product.name)
            product.save()

            return redirect('seller_dashboard')

    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form':form})