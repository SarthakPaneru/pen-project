from django import forms
from django.forms import fields, widgets
from .models import Product

# create model form
class AddProductForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Product
        fields = [
            "name",
            "price",
            "desc",
            "stock",
            "image",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Name"
                },
                
            ),
            
            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Price",
                }
            ),
            "desc": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Description",
                }
            ),
            "stock": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Stock",
                }
            ),
            "image": forms.ClearableFileInput(
                attrs={
                    "class": "btn btn-light"
                }
            )
            
        }

class editProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "price",
            "desc",
            "stock",
        ]

class AddProductImgForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["image",]

        widgets = {
            "image": forms.ClearableFileInput(
                attrs={
                    "class": "btn btn-light",
                    "placeholder": "Image",
                }
            )
        }
