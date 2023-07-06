from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


class CartView(APIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        cart = Cart.objects.get(user_id=request.user)
        serializer = self.serializer_class(cart)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        sub_serializer = CartItemSerializer(many=True,data=request.data['cart_items'])
        
        if serializer.is_valid() and sub_serializer.is_valid():
                sub_serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)