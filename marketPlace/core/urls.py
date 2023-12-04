from django.urls import path,include

# never do this in production
from django.conf import settings
from django.conf.urls.static import static
# never !! it's just to make the image appear

from django.contrib.auth import views as auth_views
from .forms import(
    LoginForm,
)
from .views import(
    index,
    contact,
    signup,
)

app_name = "core"

urlpatterns = [
    path("",index, name="index"),
    path("contact/",contact, name="contact"),
    path("signup/", signup, name="signup"),
    path("login/",auth_views.LoginView.as_view(template_name="core/login.html" ,authentication_form=LoginForm), name="login")
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)