from django.contrib import admin
from django.urls import path
from . views import product_list, product_detail, home

app_name = "market"
urlpatterns = [
    path('',home, name="home"),
    path('products/',product_list, name="product_list"),
    path('category/<slug:category_slug>/',product_list, name="products_category"),
    path('detail/<slug:product_slug>/',product_detail, name="product_detail"),
]


