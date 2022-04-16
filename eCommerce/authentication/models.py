from itertools import product
from django.db import models
from django.contrib.auth.models import User

# from home.models import Product

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='images', null=True, blank=True)
    contact = models.CharField(max_length=15, blank=True)
    # product = models.ManyToManyField(Product, on_delete=models.SET_NULL, null=True, blank=True)
    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username


#   dont make many table for auth user model
#
# class Customer(Profile):
#     customer = models.OneToOneField(Profile, on_delete=models.CASCADE)
#     customer.is_customer = True

#     def __str__(self) -> str:
#         return self.customer.username

# class Seller(Profile):
#     seller = models.OneToOneField(Profile, on_delete=models.CASCADE)
#     seller.is_seller = True

#     def __str__(self) -> str:
#         return self.seller.username