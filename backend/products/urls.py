from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    path('products/', views.ProductsView.as_view()),
    path('products/<int:pk>/', views.ProductView.as_view(), name="products-detail"),
    path('categories/', views.CategoriesView.as_view()),
    path('categories/<int:pk>/', views.CategoryView.as_view(), name="category-details"),
]