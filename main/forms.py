from django import forms
from main.models import Product

class ProductForm(forms.ModelForm):
    SIZE_CHOICES = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]
    
    size = forms.ChoiceField(choices=SIZE_CHOICES)

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'size']