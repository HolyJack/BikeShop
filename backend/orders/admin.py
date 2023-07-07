from django.contrib import admin
from .models import *


class ShippingMethodAdmin(admin.ModelAdmin):
    pass


class ShopOrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(ShippingMethod, ShippingMethodAdmin)
admin.site.register(ShopOrder, ShopOrderAdmin)
