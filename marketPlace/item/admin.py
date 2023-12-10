from django.contrib import admin
from .models import(
    Category,
    Item,
    ShoppingCart,
    CartItem,
)

# Register your models here.
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(ShoppingCart)
admin.site.register(CartItem)