from django.urls import path
from home.views import about, addProduct, addProductPage, addToCart, cart, category, decProductInCart, delete_cart, editProduct, editProductImg, incProductInCart, index, individualProduct, postComment, search, seller, test, verify_payment

urlpatterns = [
    path('', index, name='home'),
    path('seller', seller, name='seller'),
    path('add-product', addProductPage, name='addProductPage'),
    path('product-added', addProduct, name='addProduct'),
    path('edit-product/<int:pk>', editProduct, name='editProduct'),
    path('edit-product-img/<int:pk>', editProductImg, name='editProductImg'),
    path('category', category, name='category'),
    path('about', about, name='about'),
    path('indivProduct/<int:pk>', individualProduct, name='individualProduct'),
    path('search', search, name='search'),
    path('cart/<str:username>', cart, name='cart'),
    path('cart-added/<int:pk>', addToCart, name='addToCart'),
    path('test', test, name='test'),
    path('comment-posted/<int:pk>', postComment, name='postComment'),
    path('cart/<int:pk>', incProductInCart, name='incProductInCart'),
    path('cart/dec/<int:pk>', decProductInCart, name='decProductInCart'),
    path('api/verify-payment', verify_payment, name='verify_payment'),
    path('delete/cart/<int:pk>', delete_cart, name='delete_cart'),
]
