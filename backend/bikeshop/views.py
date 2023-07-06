from django.contrib.auth import login, logout
from rest_framework import viewsets, permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.db import connection


class UserRegisterView(APIView):
    serializer = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        data = request.data
        serializer = self.serializer(data=data)
        
        print('wow')
        if not serializer.is_valid(raise_exception=True):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        email = data['email']
        if not data['email'] or User.objects.filter(email=email).exists():
            return Response({'email': [
                'User already exists'
                ]}, status=status.HTTP_400_BAD_REQUEST)
    
        serializer.create(data)
            
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    serializer = UserLoginSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [SessionAuthentication]
    
    def post(self, request):
        data = request.data
        serializer = self.serializer(data=data)
        
        if serializer.is_valid(raise_exception=True):
            print('valid')
            user = serializer.check_user(request)
            print('valid')
            login(request, user)
            
            return Response({'message': 'Login succesful.'}, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class UserView(APIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)
    
    def patch(self, request):
        serializer = self.serializer_class(request.user, data=request.data)
        if serializer.is_valid():
            serializer.update(request.user, validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
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

