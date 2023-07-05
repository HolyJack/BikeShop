from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.db import connection


class UserRegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        data = request.data
        serializer = UserRegisterSerializer(data=data)
        
        if not serializer.is_valid(raise_exception=True):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        email = data['email']
        if not data['email'] or User.objects.filter(email=email).exists():
            return Response({'email': [
                'User already exists'
                ]}, status=status.HTTP_400_BAD_REQUEST)
    
        serializer.create(data)
            
        return Response(serializer.data, status=status.HTTP_201_CREATED)
            


class UserLogin(APIView):
    pass
    

class UserLogout(APIView):
    pass


class UserView(APIView):
    pass


# API for Product fields

class ProductCategoryView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()
  
    
class VariationView(viewsets.ReadOnlyModelViewSet):
    serializer_class = VariationSerializer
    queryset = Variation.objects.all()
  
    
class VariationOptionView(viewsets.ReadOnlyModelViewSet):
    serializer_class = VariationOptionSerializer
    
    def get_queryset(self):
        queryset = VariationOption.objects.all()
        queryset = VariationOptionSerializer.setup_eager_loading(queryset)
        return queryset
    
class ProductView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductItemView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductItemSerializer
    queryset = ProductItem.objects.all()

#

class UserRegistrationView(viewsets.ModelViewSet):
    pass