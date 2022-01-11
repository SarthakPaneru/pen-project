from django.shortcuts import redirect, render
from authentication.models import Profile
from home.models import Product
from .forms import AddProductForm 
from django.contrib.auth.decorators import login_required
from authentication.models import Profile
from django.contrib.auth.models import User


# Create your views here.

# Home
def index(request):
    return render(request, 'index.html')

# Seller Page
def seller(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'seller.html', context)

# add Product page
#@login_required
def addProductPage(request):
    form = AddProductForm()
    context = {
        'form': form
    }
    return render(request, 'add_product.html', context)

# add Product form submission
def addProduct(request):
    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():           
            print(request.user.username)
            #seller = Profile.objects.get(user=User.objects.get(username=request.user.username))
            #print(seller)
            form.cleaned_data['seller'] = request.user.profile
            Product.objects.create(**form.cleaned_data) # ** le dictionary ma throw gareko value harulai catch garxa
            return redirect('seller')
    else:
        return redirect('addProductPage')
    return render(request, 'add_product.html', {'form': form})
