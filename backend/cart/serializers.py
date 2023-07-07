from rest_framework import serializers
from .models import *

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
        read_only_fields = ['id', 'cart_id']


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Cart
        fields = ['id', 'user_id', 'cart_items']
        read_only_fields = ['id', 'user_id']
        
    