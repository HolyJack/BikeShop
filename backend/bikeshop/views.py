from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *


# API for Product fields

class ProductCategoryView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()
  
    
class VariationView(viewsets.ReadOnlyModelViewSet):
    serializer_class = VariationSerializer
    queryset = Variation.objects.all()
  
    
class VariationOptionView(viewsets.ReadOnlyModelViewSet):
    serializer_class = VariationOptionSerializer
    queryset = VariationOption.objects.all()
  
    
class ProductView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductItemView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductItemSerializer
    queryset = ProductItem.objects.all()

#