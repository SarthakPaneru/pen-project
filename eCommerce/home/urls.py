from django.urls import path
from home.views import about, addProduct, addProductPage, category, editProduct, editProductImg, index, individualProduct, search, seller

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
    path('p', search, name='search'),
]
