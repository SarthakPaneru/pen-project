from django.shortcuts import redirect, render
from authentication.models import Profile
from home.models import Cart, Comment, Product
from .forms import AddProductForm, AddProductImgForm, editProductForm 
from django.contrib.auth.decorators import login_required
from authentication.models import Profile
from django.contrib.auth.models import User


# Create your views here.

# Home
def index(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'index.html', context)

# Seller Page
@login_required
def seller(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'seller.html', context)

# add Product page
@login_required
def addProductPage(request):
    form = AddProductForm()
    context = {
        'form': form
    }
    return render(request, 'add_product.html', context)

# add Product form submission
@login_required
def addProduct(request):
    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES)
        #img_form = AddProductImgForm(request.POST, request.FILES)
        # print(form.errors)
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

# display information about the product in seller page
@login_required
def editProduct(request, pk):
    product = Product.objects.get(pk = pk)
    if product.seller.user == request.user:
        form = editProductForm(initial={'name': product.name, 'price': product.price, 'desc': product.desc, 'stock': product.stock})
        context = {
            'form': form,
            'product': product
        }
        if request.method == 'POST' and 'button' in request.POST:
            form = editProductForm(request.POST)
            if form.is_valid():
                product.name, product.price, product.desc, product.stock = form.cleaned_data.values()
                product.save()
                return redirect('seller')
    else:
        return redirect('home')
    return render(request, 'editProduct.html', context)

@login_required
def editProductImg(request, pk):
    product = Product.objects.get(pk = pk)
    if product.seller.user == request.user:
        
        if request.method == 'POST':
            image = request.FILES.get('image')
            product.image = image
            product.save()
            return redirect('seller')
    else:
        return redirect('home')
    return render(request, 'editProduct.html')

# Prodeuct page for categories
def category(request):
    return render(request, 'product.html')

# About Page
def about(request):
    return render(request, 'about.html')

# Individual product display
def individualProduct(request, pk):
    product = Product.objects.get(pk = pk)
    context = {
        'product': product
    }
    return render(request, 'individualProduct.html', context)

# search Query
def search(request):
    str = request.POST.get('query')
    print(str)
    products = Product.objects.all().filter(name__icontains = str)
    print(products)
    context = {
        'products': products
    }
    return render(request, 'search.html', context)

# views for cart system
def cart(request):
    carts = Cart.objects.all()
    context = {
        'carts': carts
    }
    return render(request, 'cart.html', context)

# add to cart
def addToCart(request, pk):
    product = Product.objects.get(pk = pk)

    if request.method == 'POST':
        cart.product = product
        cart.total += 1 
        cart.save()

# comment section
@login_required
def postComment(request, pk):
    str = request.POST.get('userComment')
    
    if request.method == 'POST':
        Comment.comment = str
        Comment.profile = request.user
        Comment.save()
        return render(request, 'individualProduct.html')
    return render(request, 'individualProduct.html')

def test(request):
    return render(request, 'test.html')