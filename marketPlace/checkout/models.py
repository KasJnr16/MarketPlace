from django.db import models
from django.contrib.auth.models import User
import random
from item.models import ShoppingCart


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Address"

    def __str__(self):
        return f"{self.street}, {self.city}, {self.region} {self.zip_code}"

class Checkout(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f"Checkout for {self.user.username}"

# class Delivery(models.Model):
#     for_user = models.OneToOneField(User, on_delete=models.CASCADE)
#     checkout = models.ForeignKey(Checkout, related_name='deliveries', on_delete=models.PROTECT)
#     shopping_cart = models.ForeignKey(ShoppingCart, related_name='deliveries', on_delete=models.PROTECT)
#     shipping_address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
#     status = models.CharField(max_length=30, default="pending")
   