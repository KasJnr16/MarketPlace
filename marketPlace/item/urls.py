from django.urls import path
from .views import(
    detail
)

# adding a name space
app_name = "item"

urlpatterns = [
    path("<int:pk>/",detail, name="detail"),
]