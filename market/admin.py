from django.contrib import admin

from . models import Product, Category,Brand, ProductImage


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductImage)
