from django.db import models

from django.db import models
from django.urls import reverse
from seller.models import Seller

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True) 
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("eshop:product_list_by_category", args=[self.slug])
     

class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller,related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='media/%y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    weight = models.IntegerField(blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id','slug'),)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("eshop:product_detail", args=[self.id, self.slug])

#For posting differnt image alonside with different colour
class PostImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/%y/%m/%d',blank=True)
    
    def __str__(self):
        return self.product.name

#For size variant available
class PostSize(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    size = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.product.name

#For Colour variant available
class PostColor(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    color = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.product.name


