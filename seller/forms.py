from django.forms import ModelForm
from eshop.models import Product

class ProductForm(ModelForm):
    class Meta():
        model = Product
        fields = ['category','name','image','description','price','weight']