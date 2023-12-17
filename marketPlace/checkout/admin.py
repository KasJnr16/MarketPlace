from django.contrib import admin
from .models import(
    Checkout,
    Address,
)

# # Register your models here.
admin.site.register(Checkout)
admin.site.register(Address)