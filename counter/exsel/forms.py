from django.forms import ModelForm

from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'composition', 'price', 'grams_per_person', 'weight', 'rubric')
