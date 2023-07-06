from django.contrib import admin
from .models import *


class ProductCategoryAdmin(admin.ModelAdmin):
    pass

class VariationAdmin(admin.ModelAdmin):
    pass

class VariationOptionAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    pass

class ProductItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(VariationOption, VariationOptionAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductItem, ProductItemAdmin)