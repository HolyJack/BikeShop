from django.contrib import admin
from .models import *

class CartItemAdmin(admin.ModelAdmin):
    pass


class CartItemInLine(admin.TabularInline):
    model = CartItem


class CartAdmin(admin.ModelAdmin):
    inlines = [
        CartItemInLine,
    ]

admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Cart, CartAdmin)