from django.contrib import admin
from .models import PaymentMethod


class PaymentMethodAdmin(admin.ModelAdmin):
    pass


admin.site.register(PaymentMethod, PaymentMethodAdmin)
