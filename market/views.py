from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import  Count
from django.db.models import Q

from . models import Product, ProductImage, Category, ProductView


def home(request):
    categories = Category.objects.all()
    most_recent = Product.objects.order_by('-created')[0:12]
    
    context = {
        'categories': categories, 
        'most_recent': most_recent
    }
    return render(request, "market/home.html", context)


def product_list(request, category_slug = None):
    category = None 
    products = Product.objects.all()
    categories = Category.objects.annotate(total_products = Count('product') )

    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = products.filter(category=category)

    search_query = request.GET.get('q')
    if search_query:
        products = products.filter(
            Q(name__icontains = search_query)|
            Q(description__icontains = search_query)|
            Q(brand__name__icontains = search_query) |
            Q(category__name__icontains = search_query)|
            Q(condation__icontains = search_query)
        )


    paginator = Paginator(products, 1)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    
    context = {
        'products': products,
        'categories': categories,
        'category': category,
    }

    return render(request, "market/product_list.html", context)


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    images  = ProductImage.objects.filter(product=product)
    
    if request.user.is_authenticated:
        ProductView.objects.get_or_create(user=request.user, product=product)
    context = {
        'product': product,
        'images' : images
    }
    return render(request, "market/product_detail.html", context)

