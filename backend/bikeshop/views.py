from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

class TireView(viewsets.ModelViewSet):
    serializer_class = TireSerializer
    queryset = Tire.objects.all()

class FrameView(viewsets.ModelViewSet):
    serializer_class = FrameSerializer
    queryset = Frame.objects.all()

class SeatView(viewsets.ModelViewSet):
    serializer_class = SeatSerializer
    queryset = Seat.objects.all()


class WheelView(viewsets.ModelViewSet):
    serializer_class = WheelSerializer
    queryset = Wheel.objects.all()

class BikeView(viewsets.ModelViewSet):
    serializer_class = BikeSerializer
    
    def get_queryset(self):
        queryset = Bike.objects.all()
        queryset = BikeSerializer.setup_eager_loading(queryset)
        return queryset
