from django.db import models
from authentication.models import Profile
from django.contrib.auth.models import User
from datetime import date
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Product(models.Model):
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=50)
    image= models.ImageField(upload_to='images/')
    price = models.DecimalField(decimal_places=2, max_digits=8)    # Always store money in DecimalField
    desc = models.TextField()
    stock = models.IntegerField()
    rating = models.IntegerField(blank=True, null=True)
    # comment = models.ForeignKey(Comment, on_delete=models.SET_NULL, blank=True, null=True)    -- Wrong way

    def __str__(self):
        return str(self.name)

# Comment
class Comment(models.Model):
    comment = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=False) # one profile has many comments
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # One product can have many comments & if product is deleted so is comment
    # date = models.DateField(_("Date"), default=date.today)

    def __str__(self):
        return str(self.comment)

#
class Cart(models.Model):
    total = models.IntegerField(default=1)
    totalPrice = models.DecimalField(default=1.00, decimal_places=2, max_digits=8)
    # grandTotal = models.DecimalField(default=0.00, decimal_places=2, max_digits=8)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.product)

class CustomerCart(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self)

