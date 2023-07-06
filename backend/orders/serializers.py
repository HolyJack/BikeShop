from rest_framework import serializers
from .models import *

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        exclude = ['id']


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True)
    
    class Meta:
        model = Cart
        fields = ['id', 'user_id', 'cart_items']
        
    