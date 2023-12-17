# checkout/urls.py
from django.urls import path
from .import views

app_name = 'checkout'

urlpatterns = [
    path("checkout-detail/<int:shopping_cart_pk>", views.checkout_details, name="checkout_detail"),
    path("success",views.checkout_success, name="checkout_success"),
    path("add-to-checkout/<int:shoppingCart_id>/",views.add_to_checkout, name="add_to_checkout"),

]
