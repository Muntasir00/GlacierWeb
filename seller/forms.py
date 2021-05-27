from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from .models import Seller
from eshop.models import Product

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(required=True, input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = User
        fields = ['username', 'email', 'date_of_birth', 'password1', 'password2']
        

    def save(self, commit=True):
        date_of_birth = self.cleaned_data.pop('date_of_birth', None)
        user = super(UserRegisterForm, self).save(commit)
        seller = Seller.objects.create(name=user.username, date_of_birth=date_of_birth, created_by=user)
        return user

class ProductForm(ModelForm):
    class Meta():
        model = Product
        fields = ['category','name','image','description','price','weight']