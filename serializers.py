from rest_framework import serializers
from .models import Bike, Order

class BikeSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Bike
        fields = ("id", "name", "description", "frame", "tires", "seat", "has_basket")
        
class OrderSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Order
        fields = ("id", "fullname", "phone_number", "bike", "status")