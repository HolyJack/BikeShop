from rest_framework import serializers
from .models import *


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'parent_category_id', 'name']


class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variation
        fields = ['id', 'category_id', 'name']
        

class VariationOptionSerializer(serializers.ModelSerializer):
    variation_id = VariationSerializer()
    
    class Meta:
        model = VariationOption
        fields = ['id', 'variation_id', 'value']
        
    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related('variation_id')
        
        return queryset


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = [
            'id',
            'product_id',
            'sku',
            'qty_in_stock',
            'img',
            'price',
            'variation'
            ]

