from rest_framework import generics, permissions
from .models import ShopOrder
from .serializers import ShopOrderSerializer


class ShopOrdersView(generics.ListCreateAPIView):
    queryset = ShopOrder.objects.all()
    serializer_class = ShopOrderSerializer
    permission_classes = [permissions.IsAdminUser]
    

class ShopOrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShopOrder.objects.all()
    serializer_class = ShopOrderSerializer
    permission_classes = [permissions.IsAdminUser]
