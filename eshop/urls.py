from django.urls import path
from . import views

app_name = 'eshop'

urlpatterns = [
    path('',views.product_list, name='product_list'),
    path('all_product/',views.all_product, name='all_product'),
    #path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<slug:category_slug>/', views.all_product, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,name='product_detail'),
    ]