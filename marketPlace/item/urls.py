from django.urls import path
from .views import(
    detail,
    newitem,
    delete,
    edit,
    items,
)

# adding a name space
app_name = "item"

urlpatterns = [
    path("",items, name = "items"),
    path("new-item/",newitem, name="newitem"),
    path("<int:pk>/",detail, name="detail"),
    path("<int:pk>/delete",delete, name="delete"),
    path("<int:pk>/edit",edit, name="edit"),
    
]