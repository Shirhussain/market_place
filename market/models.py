from django.db import models
from django.contrib.auth.models import  User
from django.utils import timezone

class Product(models.Model):
    
    CONDATION_TYPE = (
        ('New','New'),
        ('Used','Used'),

    )
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # when you set_null so apply null=True as well
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    condation = models.CharField(max_length=4, choices=CONDATION_TYPE)
    created = models.DateTimeField(default=timezone.now)


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

