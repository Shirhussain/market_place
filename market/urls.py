from django.contrib import admin
from django.urls import path
from . views import product_list, product_detail

app_name = "market"
urlpatterns = [
    path('',product_list, name="product_list"),
    path('<slug:product_slug>/',product_detail, name="product_detail"),
]


