from django.contrib import admin
from .models import UserPaymentMethod


class PaymentMethodAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserPaymentMethod, PaymentMethodAdmin)
