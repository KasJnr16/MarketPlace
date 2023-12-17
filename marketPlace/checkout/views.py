from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Checkout, Address
from item.models import ShoppingCart, CartItem

@login_required
def add_to_checkout(request, shoppingCart_id):
    address = get_object_or_404(Address, user=request.user)
    user_shopping_cart = get_object_or_404(ShoppingCart, user=request.user, pk=shoppingCart_id)
    checkout, created = Checkout.objects.get_or_create(
        user=request.user,
        shipping_address=address,
        shopping_cart = user_shopping_cart,
        defaults={'is_completed': True},  # Set default values for the created object
    )

    if not isinstance(checkout, Checkout):
        checkout = checkout.first()

    # user_shopping_cart.cartitem_set.all().delete()
    return redirect("checkout:checkout_detail", shopping_cart_pk=shoppingCart_id)

@login_required
def checkout_details(request, shopping_cart_pk):
    address = get_object_or_404(Address, user=request.user)
    shopping_cart = get_object_or_404(ShoppingCart, user=request.user, pk=shopping_cart_pk)
    cart_items = CartItem.objects.filter(cart=shopping_cart)
    checkout = get_object_or_404(Checkout, shopping_cart=shopping_cart, shipping_address=address)

    return render(request, "checkout/checkout.html", {
        "checkout": checkout,
        "cart_items": cart_items,
    })

@login_required
def checkout_success(request):
    return render(request, 'checkout/checkout_success.html', {})
