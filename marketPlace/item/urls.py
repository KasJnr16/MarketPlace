from django.urls import path
from .views import(
    detail,
    newitem,
)

# adding a name space
app_name = "item"

urlpatterns = [
    path("new-item/",newitem, name="newitem"),
    path("<int:pk>/",detail, name="detail"),
]