from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.CartView.as_view()),
    path('cart/<int:id>/', views.CartItemView.as_view(), name='cart_item')
]