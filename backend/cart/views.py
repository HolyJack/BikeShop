from rest_framework import permissions, status, generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsCartOwner, IsCartItemOwner
from .serializers import *
from .models import *

# class CartView(APIView):
#     serializer_class = CartSerializer
#     permission_classes = [permissions.IsAuthenticated, IsCartOwnerOrAdmin]
    
#     def get(self, request):
#         cart = Cart.objects.get(user_id=request.user)
#         serializer = self.serializer_class(cart)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         sub_serializer = CartItemSerializer(many=True,data=request.data['cart_items'])
        
#         if serializer.is_valid() and sub_serializer.is_valid():
#                 sub_serializer.save()
#                 return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# class CartItemView(APIView):
#     permission_classes = [permissions.IsAuthenticated, IsCartOwnerOrAdmin]
    
#     def get(self, request, id):
#         try:
#             cart_item = CartItem.objects.get(id=id)
#         except CartItem.DoesNotExist:
#             return Response("Cart item not found", status=status.HTTP_404_NOT_FOUND)
        
#         serializer = CartItemSerializer(cart_item)
        
#         return Response(serializer.data)
        
    
#     def put(self, request, id):
#         try:
#             cart_item = CartItem.objects.get(id=id)
#         except CartItem.DoesNotExist:
#             return Response("Cart item not found", status=status.HTTP_404_NOT_FOUND)

#         if cart_item.cart_id.user_id != request.user:
#             return Response(status=status.HTTP_403_FORBIDDEN)
        
#         serializer = CartItemSerializer(cart_item, data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
#     def delete(self, request, id):
#         try:
#             cart_item = CartItem.objects.get(id=id)
#         except CartItem.DoesNotExist:
#             return Response("Cart item not found", status=status.HTTP_404_NOT_FOUND)

#         cart_item.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework import generics
from .models import Cart, CartItem
from .serializers import CartSerializer


class CartView(generics.RetrieveUpdateAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated, IsCartOwner]

    def get(self, request):
        cart = Cart.objects.get(user_id=request.user)
        serializer = self.serializer_class(cart)
        return Response(serializer.data)
    
    
class CartItemView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated, IsCartItemOwner]
    
    
    def get(self, request):
        cart_item = CartItem.objects.get(cart_id=request.user.cart_id)
        serializer = self.serializer_class(cart_item)
        return Response(serializer.data)
    
    
    def put(self, request):
        #qty = request.data.get('qty')
        cart_item = CartItem.objects.get(cart_id=request.user.cart_id)
        serializer = self.serializer_class(cart_item)
        return Response(serializer.data)        
    