from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .constants.constants import *
from .constants.countries import COUNTRIES
from phonenumber_field.modelfields import PhoneNumberField


class TimeStampedModel(models.Model):
    date_added =  models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    
    class Meta:
        abstract = True


#   Product Models


class ProductCategory(TimeStampedModel, models.Model):
    parent_category_id = models.ForeignKey("ProductCategory", on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = 'Product categories'
        
    def __str__(self):
        return self.name
    
    
class Variation(TimeStampedModel, models.Model):
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class VariationOption(TimeStampedModel, models.Model):
    variation_id = models.ForeignKey(Variation, on_delete=models.CASCADE) 
    value = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.variation_id.name}: {self.value}"
  
    
class Product(TimeStampedModel, models.Model):
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=255)
    product_image = models.URLField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.name


class ProductItem(TimeStampedModel, models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    sku = models.CharField("SKU", max_length=255, blank=True, null=True)
    qty_in_stock = models.PositiveIntegerField()
    img = models.URLField(max_length=200, blank=True)
    price = models.DecimalField("Price", max_digits=5, decimal_places=2)
    variations = models.ManyToManyField(VariationOption, blank=True)
    
    def __str__(self):
        return f'{self.product_id.name} {self.sku} {self.qty_in_stock}'

#   User Models

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self.create_user(email, password, **extra_fields)
        

class User(AbstractBaseUser, PermissionsMixin):
    username = None
    first_name = models.CharField(max_length=1024, blank=True, null=True)
    last_name = models.CharField(max_length=1024, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True)
    phonenumber = PhoneNumberField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_added =  models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    def __str__(self):
        return self.email

class UserAdress(TimeStampedModel, models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    is_default = models.BooleanField(default=False)
    name = models.CharField(max_length=1024)
    address1 = models.CharField(max_length=1024)
    address2 = models.CharField(max_length=1024)
    zip_code = models.CharField(max_length=12)
    city = models.CharField(max_length=1024)
    region = models.CharField(max_length=1024)
    country = models.CharField(max_length=3, choices=COUNTRIES)
    
    def save(self, *args, **kwargs) -> None:
        if not UserAdress.objects.filter(user_id=True).exists():
            self.is_default = True
        super().save(*args, **kwargs)