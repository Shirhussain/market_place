from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import  Count
from . models import Product, ProductImage, Category

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.annotate(total_products = Count('product') )

    paginator = Paginator(products, 10)

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    
    context = {
        'products': products,
        'categories': categories
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

