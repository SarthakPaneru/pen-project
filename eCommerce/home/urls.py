from django.urls import path
from home.views import about, addProduct, addProductPage, addToCart, cart, category, editProduct, editProductImg, index, individualProduct, postComment, search, seller, test

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
    path('cart', cart, name='cart'),
    path('cart-added', addToCart, name='addToCart'),
    path('test', test, name='test'),
    path('comment-posted/<int:pk>', postComment, name='postComment'),
]
