from django.db import models
from django.contrib.auth.models import  User
from django.utils import timezone
from django.utils.text import  slugify

class Product(models.Model):
    
    CONDATION_TYPE = (
        ('New','New'),
        ('Used','Used'),

    )
    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(editable=False)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='Product_main_image/%Y/', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True )
    # when you set_null so apply null=True as well
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    condation = models.CharField(max_length=4, choices=CONDATION_TYPE)
    created = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)



    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Category_image/%Y/%m/%d')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image   = models.ImageField(upload_to="product_image/%Y/", blank=True, null=True)

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"

    def __str__(self):
        return self.product.name
