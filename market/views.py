from django.shortcuts import render, get_object_or_404
from . models import Product, ProductImage

def product_list(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, "market/product_list.html", context)


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    images  = ProductImage.objects.filter(product=product)
    print(images)
    
    context = {
        'product': product,
        'images' : images
    }
    return render(request, "market/product_detail.html", context)

