from django.db import models


class Cart(models.Model):
    user_id = models.ForeignKey("accounts.User", auto_created=True ,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'

class CartItem(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product_item_id = models.ForeignKey("products.ProductItem", on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()
