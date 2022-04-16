import decimal
from urllib import response
from django.http import JsonResponse
from django.shortcuts import redirect, render
from authentication.models import Profile
from home.models import Cart, Comment, Product
from .forms import AddProductForm, AddProductImgForm, editProductForm 
from django.contrib.auth.decorators import login_required
from authentication.models import Profile
from django.contrib.auth.models import User
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt


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
        'products': products,
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
    disc = product.price * decimal.Decimal(1.25)

    comments = Comment.objects.filter(product_id = pk)

    # comments = product.comment
    context = {
        'product': product,
        'discs' : disc,
        # 'comments': comments

        'comments': comments
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
@login_required
def cart(request, username):
    carts = Cart.objects.filter(customer_username = username)
    print(carts)
    #   print(carts.first().customer)   # prints first data of queryset
    grandTotal = 0
    print(request.user)
    for cart in carts:
        print(cart.customer.user)
        if (cart.customer.user == request.user):
            print('Good')
            cart.totalPrice = cart.product.price * cart.total
            grandTotal += cart.totalPrice
            print(cart.totalPrice)

    grandTotal *= 100 # as khalti accepts in paisa 
    context = {
        'carts': carts,
        'grandTotal': grandTotal
    }
    return render(request, 'cart.html', context)

def incProductInCart(request, pk):

    if request.method == 'POST':
        if (Cart.objects.filter(product_id = pk)):
            Cart.objects.filter(product_id = pk).update(total=F('total')+1)
            print('Increase')
        return redirect('cart')
    return render(request, 'cart.html')

def decProductInCart(request, pk):

    if request.method == 'POST':
        if (Cart.objects.filter(product_id = pk)):
            cart = Cart.objects.get(product_id = pk)
            print('decrease')
            if cart.total != 0:
                Cart.objects.filter(product_id = pk).update(total=F('total')-1)
            return redirect('cart')
    return render(request, 'cart.html')

# add to cart
@login_required
def addToCart(request, pk):
    product = Product.objects.get(pk = pk)

    if request.method == 'POST':
        cart = Cart()
        # idCompare = 
        if (Cart.objects.filter(product_id = pk)):
            # cart.product = product
            Cart.objects.filter(product_id = pk).update(total=F('total')+1)
            # cart.total = cart.total + 1   -> Yesari garne haine mathi jasari garne use 'F' {import django.db.models}
        else:
            cart.product = product
            profile = Profile.objects.get(user = request.user)
            cart.customer = profile
            cart.save()
            
            
            
        
        return redirect('individualProduct', pk)    # we must redirect here or error arises
    return render(request, 'individualProduct.html')

@login_required
def delete_cart(request, pk):
    cart = Cart.objects.get(pk = pk)

    if request.method == 'POST':
        cart.delete()

        return redirect('cart')
    return render(request, 'cart.html')

# comment section
@login_required
def postComment(request, pk):
    str = request.POST.get('userComment')
    
    if request.method == 'POST':
        product = Product.objects.get(pk = pk)  # kun product ko comment ho define garnu parxa
        comment = Comment()
        comment.comment = str
        profile = Profile.objects.get(user = request.user)
        comment.profile = profile        
        comment.product = product
        
        comment.save()  # we should first save comment        

        return redirect('individualProduct', pk)
    return render(request, 'individualProduct.html')

def test(request):
    return render(request, 'test.html')

@csrf_exempt
def verify_payment(request):
    import requests, json

    data = request.POST
    product_id = data['product_identity']
    token = data['token']
    amount = data['amount']

    url = 'https://khalti.com/api/v2/payment/verrify/'
    payload = {
        'token': token,
        'amount': amount
    }
    headers = {
        'Authorization': 'Key test_secret_key_7e362c26c5a14cfb803cae48d46ac04e'
    }

    response = requests.post(url, payload, headers = headers)

    response_data = json.loads(response.text)
    status_code = str(response.status_code)

    if status_code == '400':
        response = JsonResponse({'status': 'false', 'message': response_data['detail']}, status=500)
        return response

    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(response_data)

    return JsonResponse(f"Payment Done !! {response_data['user']['idx']}", safe=False)