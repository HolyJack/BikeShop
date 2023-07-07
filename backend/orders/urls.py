from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.ShopOrdersView.as_view(), name='orders-list'),
    path('orders/<int:pk>/', views.ShopOrderView.as_view(), name='order-details')
]