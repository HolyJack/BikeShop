from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'product_categories', views.ProductCategoryView, 'product_category')
router.register(r'variations', views.VariationView, 'variation')
router.register(r'variation_options', views.VariationOptionView, 'variation_options')
router.register(r'product', views.ProductView, 'product')
router.register(r'product_items', views.ProductItemView, 'product_items')

urlpatterns = [
    path('api/', include(router.urls)),
]