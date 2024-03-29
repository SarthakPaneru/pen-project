from django.db import models
from authentication.models import Profile
from django.contrib.auth.models import User
from datetime import date
from django.utils.translation import gettext_lazy as _


# Comment
class Comment(models.Model):
    comment = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=False)
    date = models.DateField(_("Date"), default=date.today)

    def __str__(self):
        return self.profile

# Create your models here.
class Product(models.Model):
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=50)
    image= models.ImageField(upload_to='images/')
    price = models.FloatField()
    desc = models.TextField()
    stock = models.IntegerField()
    rating = models.IntegerField(blank=True, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

#
class Cart(models.Model):
    total = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def totalProduct(self, instance):
        self.total = self.total + instance.total

    def __str__(self):
        return self.total

