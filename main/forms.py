from django import forms
from main.models import Product
from django.utils.html import strip_tags

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

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description) 