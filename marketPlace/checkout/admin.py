from django.contrib import admin
from .models import(
    Checkout,
    CheckoutItem,
    Address,
)

# Register your models here.
admin.site.register(Checkout)
admin.site.register(CheckoutItem)
admin.site.register(Address)