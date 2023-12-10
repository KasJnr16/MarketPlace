from django.urls import path
from .views import(
    detail,
    newitem,
    delete,
    edit,
    items,
    add_to_cart,
    remove_from_cart,
    cart_view,
)

# adding a name space
app_name = "item"

urlpatterns = [
    path("",items, name = "items"),
    path("new-item/",newitem, name="newitem"),
    path("<int:pk>/",detail, name="detail"),
    path("<int:pk>/delete",delete, name="delete"),
    path("<int:pk>/edit",edit, name="edit"),
    path('cart/add-to-cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/', cart_view, name='cart_view'),
    
]