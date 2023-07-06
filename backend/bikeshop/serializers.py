from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password
from .models import *


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'parent_category_id', 'name']


class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variation
        fields = ['id', 'category_id', 'name']
        

class VariationOptionSerializer(serializers.ModelSerializer):
    variation_id = VariationSerializer()
    
    class Meta:
        model = VariationOption
        fields = ['id', 'variation_id', 'value']
        
    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related('variation_id')
        
        return queryset


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'category_id',
            'name',
            'product_description',
            'product_image'
            ]


class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = [
            'id',
            'product_id',
            'sku',
            'qty_in_stock',
            'img',
            'price',
            'variation'
            ]


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
    class Meta:
        model = User
        fields = ['email', 'password']
    
    def create(self, validated_data):
        
        user = User.objects.create_user(
            email=validated_data['email'], 
            password=validated_data['password']
            )
        
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
    class Meta:
        model = User
        fields = ['email', 'password']
    
    def check_user(self, request):
        email = request.data['email']
        password = request.data['password']
        
        if email and password:
            user = authenticate(request=request, username=email, password=password)
            
            if not user:
                raise serializers.ValidationError('Invalid user or password')
        else:
            raise serializers.ValidationError('Email and password are required.')
        
        return user


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    
    class Meta:
        model = User
        exclude = [
            'is_superuser',
            'is_staff',
            'groups',
            'user_permissions',
            'password'
            ]