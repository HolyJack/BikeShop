from django.db import models


class PaymentType(models.Model):
    value = models.CharField(max_length=50)


class UserPaymentMethod(models.Model):
    name = models.CharField(max_length=50)
    user_id = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    payment_type_id = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    provider = models.CharField(max_length=50)
    account_number = models.PositiveIntegerField()
    expiry_date = models.DateField(auto_now=False, auto_now_add=False)
    is_default = models.BooleanField(default=False)