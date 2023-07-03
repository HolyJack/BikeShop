from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BikeSerializer, OrderSerializer
from .models import Bike, Order

class BikeView(viewsets.ModelViewSet):
    serializer_class = BikeSerializer
    queryset = Bike.objects.all()

class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
