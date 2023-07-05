from django.db import models
from django.utils.crypto import get_random_string
from .constants import *
from phonenumber_field.modelfields import PhoneNumberField


class TimeStampedModel(models.Model):
    date_added =  models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    
    class Meta:
        abstract = True


class ProductCategory(models.Model):
    parent_category_id = models.ForeignKey("ProductCategory", on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = 'Product categories'
        
    def __str__(self):
        return self.name
    
    
class Variation(models.Model):
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class VariationOption(models.Model):
    variation_id = models.ForeignKey(Variation, on_delete=models.CASCADE) 
    value = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.variation_id.name}: {self.value}"
  
    
class Product(models.Model):
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=255)
    product_image = models.URLField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.name


class ProductItem(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    sku = models.CharField("SKU", max_length=255, blank=True, null=True)
    qty_in_stock = models.PositiveIntegerField()
    img = models.URLField(max_length=200, blank=True)
    price = models.DecimalField("Price", max_digits=5, decimal_places=2)
    variations = models.ManyToManyField(VariationOption, blank=True)
    
    def __str__(self):
        return f'{self.product_id.name} {self.sku} {self.qty_in_stock}'

