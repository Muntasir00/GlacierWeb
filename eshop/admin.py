from django.contrib import admin

from django.contrib import admin
from .models import Category, Product, PostImage

class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated', 'weight']
    list_filter = ['available','created','updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

