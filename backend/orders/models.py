from django.db import models


class Cart(models.Model):
    user_id = models.OneToOneField("accounts.User", on_delete=models.CASCADE)


class CartItem(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_item_id = models.ForeignKey("products.ProductItem", on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()


class ShippingMethod(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)


class ShopOrder(models.Model):
    PENDING = 'PE'
    PROCESSING = 'PR'
    ON_HOLD = 'OH'
    SHIPPED = 'SH'
    DELIVERED = 'DV'
    CANCELLED = 'CA'
    RETURNED = 'RE'
    REFUNDED = 'RF'

    ORDER_STATUSES = [
        (PENDING, 'Pending'),
        (PROCESSING, 'Processing'),
        (ON_HOLD, 'On Hold'),
        (SHIPPED, 'Shipped'),
        (DELIVERED, 'Delivered'),
        (CANCELLED, 'Cancelled'),
        (RETURNED, 'Returned'),
        (REFUNDED, 'Refunded'),
    ]
    
    user_id = models.ForeignKey("accounts.User", on_delete=models.PROTECT)
    order_date = models.DateField(auto_now=False, auto_now_add=True)
    order_update = models.DateField(auto_now=True, auto_now_add=False)
    payment_method = models.ForeignKey("payments.PaymentMethod", on_delete=models.PROTECT)
    shipping_adress = models.ForeignKey("accounts.UserAdress", on_delete=models.PROTECT)
    shipping_method = models.ForeignKey(ShippingMethod, on_delete=models.PROTECT)
    order_status = models.CharField(max_length=50, choices=ORDER_STATUSES)