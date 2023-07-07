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
    
    
class CartItemView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, id):
        try:
            cart_item = CartItem.objects.get(id=id)
        except CartItem.DoesNotExist:
            return Response("Cart item not found", status=status.HTTP_404_NOT_FOUND)
        
        serializer = CartItemSerializer(cart_item)
        
        return Response(serializer.data)
        
    
    def put(self, request, id):
        try:
            cart_item = CartItem.objects.get(id=id)
        except CartItem.DoesNotExist:
            return Response("Cart item not found", status=status.HTTP_404_NOT_FOUND)

        serializer = CartItemSerializer(cart_item, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, id):
        try:
            cart_item = CartItem.objects.get(id=id)
        except CartItem.DoesNotExist:
            return Response("Cart item not found", status=status.HTTP_404_NOT_FOUND)

        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)