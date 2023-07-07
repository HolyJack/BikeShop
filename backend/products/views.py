from rest_framework import viewsets, generics, permissions, status
from .serializers import *
from .models import *
from .permissions import AllowAnyReadOnlyOrStaff



class ProductsView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAnyReadOnlyOrStaff]
    

class ProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAnyReadOnlyOrStaff]
    

class CategoriesView(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = [AllowAnyReadOnlyOrStaff]


class CategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = [AllowAnyReadOnlyOrStaff]
    

