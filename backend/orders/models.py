from django.db import models


class ShippingMethod(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


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
    payment_method = models.ForeignKey("payments.UserPaymentMethod", on_delete=models.PROTECT)
    shipping_adress = models.ForeignKey("accounts.UserAdress", on_delete=models.PROTECT)
    shipping_method = models.ForeignKey(ShippingMethod, on_delete=models.PROTECT)
    order_status = models.CharField(max_length=50, choices=ORDER_STATUSES, default=ORDER_STATUSES[0])


class ShopOrderLine(models.Model):
    product_item_id = models.ForeignKey("products.ProductItem", on_delete=models.CASCADE)
    shop_order_id = models.ForeignKey(ShopOrder, on_delete=models.CASCADE, related_name='shop_order_line')
    qty = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    