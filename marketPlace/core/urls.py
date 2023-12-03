from django.urls import path,include
# never do this in production
from django.conf import settings
from django.conf.urls.static import static
# never !! it's just to make the image appear
from .views import(
    index,
    contact,
)


urlpatterns = [
    path("",index, name="index"),
    path("contact/",contact, name="contact"),
    path("items/",include("item.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)