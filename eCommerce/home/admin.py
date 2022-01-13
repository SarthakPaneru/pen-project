from django.contrib import admin
from home.models import Product, Cart, Comment

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Comment)