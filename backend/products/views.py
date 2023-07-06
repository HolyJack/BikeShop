from rest_framework import viewsets
from .serializers import *
from .models import *


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

