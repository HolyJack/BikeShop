from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from .countries import COUNTRIES
from django.apps import apps

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        
        member = apps.get_model('cart.Cart')
        member.objects.create(user_id=user)
        
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

class UserAdress(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_adresses")
    is_default = models.BooleanField(default=False)
    name = models.CharField(max_length=1024)
    address1 = models.CharField(max_length=1024)
    address2 = models.CharField(max_length=1024, blank=True)
    zip_code = models.CharField(max_length=12)
    city = models.CharField(max_length=1024)
    region = models.CharField(max_length=1024)
    country = models.CharField(max_length=3, choices=COUNTRIES)
    date_added =  models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    
    def save(self, *args, **kwargs) -> None:
        if not UserAdress.objects.filter(user_id=True).exists():
            self.is_default = True
        super().save(*args, **kwargs)

    
    def __str__(self):
        return f'{self.name}'

#from rest_framework.authtoken.models import Token

#for user in User.objects.all():
#    token = Token.objects.create(user=user)
#    print(token.key)
