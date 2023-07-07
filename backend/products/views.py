from rest_framework import viewsets, generics, permissions, status
from .serializers import *
from .models import *


# class ProductCategoryView(viewsets.ReadOnlyModelViewSet):
#     serializer_class = ProductCategorySerializer
#     queryset = ProductCategory.objects.all()
    
    
# class VariationView(viewsets.ReadOnlyModelViewSet):
#     serializer_class = VariationSerializer
#     queryset = Variation.objects.all()
  
    
# class VariationOptionView(viewsets.ReadOnlyModelViewSet):
#     serializer_class = VariationOptionSerializer
    
#     def get_queryset(self):
#         queryset = VariationOption.objects.all()
#         queryset = VariationOptionSerializer.setup_eager_loading(queryset)
#         return queryset
    
    
# class ProductView(viewsets.ReadOnlyModelViewSet):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()


# class ProductItemView(viewsets.ReadOnlyModelViewSet):
#     serializer_class = ProductItemSerializer
#     queryset = ProductItem.objects.all()

class ProductsView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    

class ProductView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    

class CategoriesView(generics.ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = [permissions.AllowAny]


class CategoryView(generics.RetrieveAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = [permissions.AllowAny]
    

