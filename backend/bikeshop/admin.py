from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm
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


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

admin.site.register(User, UserAdmin)