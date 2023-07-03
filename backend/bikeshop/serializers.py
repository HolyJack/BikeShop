from rest_framework import serializers
from .models import *
from django.db import connection

class TireSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = Tire
        fields = ("id", "name", "quantity", "type", "unit_price")
    
class FrameSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = Frame
        fields = ("id", "name", "quantity", "type", "material", "weight", "unit_price")

class SeatSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = Seat
        fields = ("id", "name", "quantity", "type", "unit_price")

class WheelSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = Wheel
        fields = ("id", "name",  "quantity", "type", "unit_price")


class BikeSerializer(serializers.ModelSerializer): 
    frame = FrameSerializer(read_only=True)
    tires = TireSerializer(read_only=True)
    seat = SeatSerializer(read_only=True)
    wheel = WheelSerializer(read_only=True)

    class Meta:
        model = Bike
        fields = ("id", "name", "quantity", "frame", "tires", "seat", "wheel", "unit_price")

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related("frame")
        print(len(connection.queries))
        queryset = queryset.select_related("tires")
        print(len(connection.queries))
        queryset = queryset.select_related("seat")
        print(len(connection.queries))
        queryset = queryset.select_related("wheel")
        print(len(connection.queries))
        
        return queryset